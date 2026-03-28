#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Iterable
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "data"
WORK.mkdir(parents=True, exist_ok=True)

TEST_URL_HTTP = "http://ip-api.com/json/?fields=status,country,countryCode,query,message"
TEST_URL_HTTPS = "https://www.naver.com/"

PROXYSCRAPE_API = "https://api.proxyscrape.com/v4/free-proxy-list/get"
PROXIFLY_KR_JSON = "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/countries/KR/data.json"
IPLOCATE_KR_TXT = "https://raw.githubusercontent.com/iplocate/free-proxy-list/main/countries/KR/proxies.txt"
GEONODE_API = "https://proxylist.geonode.com/api/proxy-list"
NIEK_FREE_PROXY_LIST = "https://niek.github.io/free-proxy-list/"
MONOSANS_KR_JSON = "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies.json"
MONOSANS_HTTP_TXT = "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt"
MONOSANS_SOCKS5_TXT = "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt"
SKILLTER_HTTP_TXT = "https://raw.githubusercontent.com/Skillter/ProxyGather/master/proxies/working-proxies-http.txt"
SKILLTER_SOCKS5_TXT = "https://raw.githubusercontent.com/Skillter/ProxyGather/master/proxies/working-proxies-socks5.txt"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)


@dataclass
class Candidate:
    source: str
    proxy: str
    protocol: str
    ip: str
    port: int
    anonymity: str = "unknown"
    source_meta: dict | None = None


@dataclass
class Result:
    source: str
    proxy: str
    protocol: str
    ip: str
    port: int
    anonymity: str
    geo_ok: bool
    https_ok: bool
    geo_time_s: float
    https_time_s: float | None = None
    geo: dict | None = None
    https_result: str | None = None
    geo_error: str | None = None
    https_error: str | None = None
    source_meta: dict | None = None
    stash_name: str | None = None


def fetch_text(url: str) -> str:
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def fetch_json(url: str, params: dict | None = None) -> dict | list:
    full_url = url if not params else f"{url}?{urlencode(params)}"
    req = Request(full_url, headers={"User-Agent": USER_AGENT, "Accept": "application/json,*/*"})
    with urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8", "replace"))


def normalize_anonymity(value: str | None) -> str:
    v = (value or "").strip().lower()
    mapping = {
        "elite": "elite",
        "hia": "elite",
        "anonymous": "anonymous",
        "anm": "anonymous",
        "transparent": "transparent",
        "noa": "transparent",
        "unknown": "unknown",
    }
    return mapping.get(v, v or "unknown")


def anonymity_rank(value: str) -> int:
    return {"elite": 0, "anonymous": 1, "unknown": 2, "transparent": 3}.get(normalize_anonymity(value), 9)


def protocol_rank(value: str) -> int:
    return {"socks5": 0, "http": 1, "socks4": 2}.get(value, 9)


def fetch_proxyscrape() -> list[Candidate]:
    payload = fetch_json(
        PROXYSCRAPE_API,
        {
            "request": "get_proxies",
            "country": "KR",
            "proxy_format": "protocolipport",
            "format": "json",
            "skip": "0",
            "limit": "100",
        },
    )
    candidates: list[Candidate] = []
    for item in payload.get("proxies", []):
        candidates.append(
            Candidate(
                source="proxyscrape",
                proxy=item["proxy"],
                protocol=item["protocol"],
                ip=item["ip"],
                port=int(item["port"]),
                anonymity=normalize_anonymity(item.get("anonymity")),
                source_meta={
                    "timeout_ms": round(float(item.get("timeout", 0) or 0), 1),
                    "city": item.get("ip_data", {}).get("city", ""),
                    "country_code": item.get("ip_data", {}).get("countryCode", ""),
                    "api": "proxyscrape_v4",
                },
            )
        )
    return candidates


def fetch_proxifly() -> list[Candidate]:
    data = fetch_json(PROXIFLY_KR_JSON)
    candidates: list[Candidate] = []
    for item in data:
        candidates.append(
            Candidate(
                source="proxifly",
                proxy=item["proxy"],
                protocol=item["protocol"],
                ip=item["ip"],
                port=int(item["port"]),
                anonymity=normalize_anonymity(item.get("anonymity")),
                source_meta={
                    "https_hint": bool(item.get("https")),
                    "score": item.get("score"),
                    "city": item.get("geolocation", {}).get("city", ""),
                    "country_code": item.get("geolocation", {}).get("country", ""),
                },
            )
        )
    return candidates


def fetch_iplocate() -> list[Candidate]:
    raw = fetch_text(IPLOCATE_KR_TXT)
    candidates: list[Candidate] = []
    for line in raw.splitlines():
        line = line.strip()
        if not line or "://" not in line:
            continue
        protocol, rest = line.split("://", 1)
        ip, port = rest.rsplit(":", 1)
        candidates.append(
            Candidate(
                source="iplocate",
                proxy=line,
                protocol=protocol,
                ip=ip,
                port=int(port),
                anonymity="unknown",
                source_meta={"country_code": "KR"},
            )
        )
    return candidates


def fetch_geonode(limit: int = 200, page: int = 1) -> list[Candidate]:
    payload = fetch_json(
        GEONODE_API,
        {
            "limit": str(limit),
            "page": str(page),
            "sort_by": "lastChecked",
            "sort_type": "desc",
            "country": "KR",
        },
    )
    candidates: list[Candidate] = []
    for item in payload.get("data", []):
        ip = item.get("ip")
        port = item.get("port")
        country = item.get("country")
        if not ip or not port or country != "KR":
            continue
        for protocol in item.get("protocols", []) or []:
            protocol = (protocol or "").lower()
            if protocol not in {"http", "socks4", "socks5"}:
                continue
            candidates.append(
                Candidate(
                    source="geonode",
                    proxy=f"{protocol}://{ip}:{port}",
                    protocol=protocol,
                    ip=ip,
                    port=int(port),
                    anonymity=normalize_anonymity(item.get("anonymityLevel")),
                    source_meta={
                        "asn": item.get("asn"),
                        "city": item.get("city"),
                        "last_checked": item.get("lastChecked"),
                        "up_time": item.get("upTime"),
                        "google_hint": item.get("google"),
                        "country_code": country,
                    },
                )
            )
    return candidates


def fetch_niek() -> list[Candidate]:
    html = fetch_text(NIEK_FREE_PROXY_LIST)
    matches = re.findall(
        r"<tr>\s*<td>(HTTP|SOCKS4|SOCKS5)</td>\s*<td>.*?South Korea.*?</td>\s*<td><code>([^<]+)</code></td>\s*<td>✅</td>",
        html,
        flags=re.I | re.S,
    )
    candidates: list[Candidate] = []
    for protocol, hostport in matches:
        if ":" not in hostport:
            continue
        ip, port = hostport.rsplit(":", 1)
        proto = protocol.lower()
        candidates.append(
            Candidate(
                source="niek",
                proxy=f"{proto}://{ip}:{port}",
                protocol=proto,
                ip=ip,
                port=int(port),
                anonymity="unknown",
                source_meta={"country_code": "KR", "status": "page_live"},
            )
        )
    return candidates


def fetch_monosans_kr_json() -> list[Candidate]:
    data = fetch_json(MONOSANS_KR_JSON)
    candidates: list[Candidate] = []
    for item in data:
        protocol = (item.get("protocol") or "").lower()
        if protocol not in {"http", "socks4", "socks5"}:
            continue
        geo = item.get("geolocation") or {}
        country = (geo.get("country") or {}).get("iso_code")
        if country != "KR":
            continue
        ip = item.get("host")
        port = item.get("port")
        if not ip or not port:
            continue
        candidates.append(
            Candidate(
                source="monosans_kr_json",
                proxy=f"{protocol}://{ip}:{port}",
                protocol=protocol,
                ip=ip,
                port=int(port),
                anonymity="unknown",
                source_meta={
                    "city": (geo.get("city") or {}).get("names", {}).get("en"),
                    "country_code": country,
                    "timeout_s": item.get("timeout"),
                },
            )
        )
    return candidates


def fetch_monosans(limit: int = 120) -> list[Candidate]:
    out: list[Candidate] = []
    for protocol, url in (("http", MONOSANS_HTTP_TXT), ("socks5", MONOSANS_SOCKS5_TXT)):
        raw = fetch_text(url)
        for line in raw.splitlines()[:limit]:
            line = line.strip()
            if not line or ":" not in line:
                continue
            ip, port = line.rsplit(":", 1)
            out.append(
                Candidate(
                    source=f"monosans_{protocol}",
                    proxy=f"{protocol}://{line}",
                    protocol=protocol,
                    ip=ip,
                    port=int(port),
                    anonymity="unknown",
                    source_meta={"generic_list": True},
                )
            )
    return out


def fetch_skillter(limit: int = 120) -> list[Candidate]:
    out: list[Candidate] = []
    for protocol, url in (("http", SKILLTER_HTTP_TXT), ("socks5", SKILLTER_SOCKS5_TXT)):
        raw = fetch_text(url)
        for line in raw.splitlines()[:limit]:
            line = line.strip()
            if not line or ":" not in line:
                continue
            ip, port = line.rsplit(":", 1)
            out.append(
                Candidate(
                    source=f"skillter_{protocol}",
                    proxy=f"{protocol}://{line}",
                    protocol=protocol,
                    ip=ip,
                    port=int(port),
                    anonymity="unknown",
                    source_meta={"generic_list": True},
                )
            )
    return out


def dedupe(candidates: Iterable[Candidate]) -> list[Candidate]:
    uniq: dict[tuple[str, str, int], Candidate] = {}
    for item in candidates:
        uniq[(item.protocol, item.ip, item.port)] = item
    return list(uniq.values())


def run_cmd(args: list[str]) -> tuple[int, str, str, float]:
    start = time.time()
    proc = subprocess.run(args, capture_output=True, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip(), time.time() - start


def build_geo_cmd(candidate: Candidate, timeout_s: int) -> list[str]:
    if candidate.protocol == "http":
        return ["curl", "-m", str(timeout_s), "-sS", "-x", candidate.proxy, TEST_URL_HTTP]
    if candidate.protocol == "socks5":
        return [
            "curl",
            "-m",
            str(timeout_s),
            "-sS",
            "--socks5-hostname",
            f"{candidate.ip}:{candidate.port}",
            TEST_URL_HTTP,
        ]
    if candidate.protocol == "socks4":
        return [
            "curl",
            "-m",
            str(timeout_s),
            "-sS",
            "--socks4a",
            f"{candidate.ip}:{candidate.port}",
            TEST_URL_HTTP,
        ]
    raise ValueError(f"unsupported protocol: {candidate.protocol}")


def build_https_cmd(candidate: Candidate, timeout_s: int) -> list[str]:
    base = ["curl", "-m", str(timeout_s), "-sS", "-I", "-L", "-o", "/dev/null", "-w", "%{http_code} %{time_total}"]
    if candidate.protocol == "http":
        return [*base, "-x", candidate.proxy, TEST_URL_HTTPS]
    if candidate.protocol == "socks5":
        return [*base, "--socks5-hostname", f"{candidate.ip}:{candidate.port}", TEST_URL_HTTPS]
    if candidate.protocol == "socks4":
        return [*base, "--socks4a", f"{candidate.ip}:{candidate.port}", TEST_URL_HTTPS]
    raise ValueError(f"unsupported protocol: {candidate.protocol}")


def status_ok(output: str) -> bool:
    code = (output.split() or ["000"])[0]
    return len(code) == 3 and code.isdigit() and code[0] in {"2", "3"}


def validate_candidate(candidate: Candidate, geo_timeout_s: int = 8, https_timeout_s: int = 12) -> Result:
    geo_rc, geo_out, geo_err, geo_dt = run_cmd(build_geo_cmd(candidate, geo_timeout_s))
    result = Result(
        source=candidate.source,
        proxy=candidate.proxy,
        protocol=candidate.protocol,
        ip=candidate.ip,
        port=candidate.port,
        anonymity=normalize_anonymity(candidate.anonymity),
        geo_ok=False,
        https_ok=False,
        geo_time_s=round(geo_dt, 3),
        source_meta=candidate.source_meta,
    )
    if geo_rc != 0:
        result.geo_error = geo_err or geo_out or f"curl exit {geo_rc}"
        return result
    try:
        geo = json.loads(geo_out)
    except Exception:
        result.geo_error = f"bad-json: {geo_out[:160]}"
        return result
    result.geo = geo
    result.geo_ok = geo.get("status") == "success" and geo.get("countryCode") == "KR"
    if not result.geo_ok:
        return result

    https_rc, https_out, https_err, https_dt = run_cmd(build_https_cmd(candidate, https_timeout_s))
    result.https_result = https_out
    result.https_error = https_err or None
    result.https_time_s = round(https_dt, 3)
    result.https_ok = https_rc == 0 and status_ok(https_out)
    return result


def pick_safe(results: list[Result]) -> list[Result]:
    safe = [r for r in results if r.anonymity in {"elite", "anonymous", "unknown"}]
    return safe or results[:]


def sort_results(results: list[Result]) -> list[Result]:
    return sorted(
        results,
        key=lambda r: (
            not r.https_ok,
            anonymity_rank(r.anonymity),
            protocol_rank(r.protocol),
            r.https_time_s if r.https_time_s is not None else 999.0,
            r.geo_time_s,
            r.ip,
            r.port,
        ),
    )


def make_name(index: int, result: Result) -> str:
    anon = result.anonymity.upper()
    proto = result.protocol.upper()
    return f"KR-{proto}-{index:02d}-{anon}-{result.ip}:{result.port}"


def render_yaml(working: list[Result], generated_at: str) -> str:
    safe = pick_safe(working)
    ordered = sort_results(working)
    safe_set = {(r.protocol, r.ip, r.port) for r in safe}

    for idx, item in enumerate(ordered, 1):
        item.stash_name = make_name(idx, item)

    lines = [
        f"# Generated at {generated_at}",
        f"# Verified through {TEST_URL_HTTP} and {TEST_URL_HTTPS}",
        "# Goal: usable KR IP proxies; Google reachability is not guaranteed.",
        "# Sources: proxyscrape, proxifly, iplocate, geonode, niek, monosans_kr_json, generic fallbacks",
        "mixed-port: 7890",
        "allow-lan: false",
        "mode: rule",
        "log-level: info",
        "",
        "proxies:",
    ]
    for item in ordered:
        lines.extend(
            [
                f"  - name: \"{item.stash_name}\"",
                f"    type: {item.protocol}",
                f"    server: {item.ip}",
                f"    port: {item.port}",
            ]
        )
        if item.protocol.startswith("socks"):
            lines.append("    udp: true")

    lines.extend(
        [
            "",
            "proxy-groups:",
            "  - name: \"节点选择\"",
            "    type: select",
            "    proxies:",
            "      - \"KR-安全自动测速\"",
            "      - \"KR-全量自动测速\"",
        ]
    )
    for item in ordered:
        lines.append(f"      - \"{item.stash_name}\"")
    lines.extend(
        [
            "      - DIRECT",
            "  - name: \"KR-安全自动测速\"",
            "    type: url-test",
            f"    url: \"{TEST_URL_HTTPS}\"",
            "    interval: 180",
            "    tolerance: 150",
            "    proxies:",
        ]
    )
    safe_names = [r.stash_name for r in ordered if (r.protocol, r.ip, r.port) in safe_set]
    if not safe_names:
        safe_names = [r.stash_name for r in ordered]
    for name in safe_names:
        lines.append(f"      - \"{name}\"")
    lines.extend(
        [
            "  - name: \"KR-全量自动测速\"",
            "    type: url-test",
            f"    url: \"{TEST_URL_HTTPS}\"",
            "    interval: 180",
            "    tolerance: 150",
            "    proxies:",
        ]
    )
    for item in ordered:
        lines.append(f"      - \"{item.stash_name}\"")

    lines.extend(["", "rules:", "  - MATCH,节点选择", ""])
    return "\n".join(lines)


def render_report(generated_at: str, per_source: dict[str, int], candidate_count: int, working: list[Result]) -> str:
    lines = [
        f"# KR 免费代理自动刷新报告（{generated_at}）",
        "",
        "> 目标：自动抓取并验证当前可用于 Stash 的韩国代理，仅在当前目录生成结果。",
        "",
        "## 采用的自动化来源",
        "",
        "1. **ProxyScrape 官方 API**  ",
        f"   - <{PROXYSCRAPE_API}?request=get_proxies&country=KR&proxy_format=protocolipport&format=json&skip=0&limit=100>",
        "2. **Proxifly 韩国国家列表**  ",
        f"   - <{PROXIFLY_KR_JSON}>",
        "3. **iplocate 韩国国家列表**  ",
        f"   - <{IPLOCATE_KR_TXT}>",
        "4. **Geonode 韩国代理 API**  ",
        f"   - <{GEONODE_API}?limit=200&page=1&sort_by=lastChecked&sort_type=desc&country=KR>",
        "5. **niek 实时页面**  ",
        f"   - <{NIEK_FREE_PROXY_LIST}>",
        "6. **monosans 带地理信息的 KR 列表**  ",
        f"   - <{MONOSANS_KR_JSON}>",
        "7. **通用列表兜底（仅在 KR 专用来源不足时测试）**  ",
        f"   - <{MONOSANS_HTTP_TXT}>  ",
        f"   - <{MONOSANS_SOCKS5_TXT}>  ",
        f"   - <{SKILLTER_HTTP_TXT}>  ",
        f"   - <{SKILLTER_SOCKS5_TXT}>",
        "",
        "## 原始候选数量",
        "",
    ]
    for source, count in sorted(per_source.items()):
        lines.append(f"- {source}: {count}")
    lines.extend([
        f"- 去重后总候选: {candidate_count}",
        "",
        "## 当前验证通过的代理",
        "",
    ])
    if not working:
        lines.append("- 本轮没有找到通过 KR 出口 + Naver HTTPS 验证的代理。")
    else:
        for idx, item in enumerate(sort_results(working), 1):
            speed = item.https_result or "N/A"
            lines.append(
                f"- {idx}. `{item.proxy}` | `{item.protocol}` | `{item.anonymity}` | {speed} | source=`{item.source}`"
            )
    lines.extend(
        [
            "",
            "## 输出文件",
            "",
            f"- Stash 配置：`{ROOT / 'stash_kr_free.yaml'}`",
            f"- 测试明细：`{WORK / 'tested_kr_proxies.json'}`",
            f"- 运行摘要：`{WORK / 'run_summary.json'}`",
            f"- 本脚本：`{WORK / 'refresh_kr_stash.py'}`",
            "",
            "## 说明",
            "",
            "- 只保留同时满足 **KR 出口** 和 **Naver HTTPS 可连** 的代理。",
            "- 当前配置的用途是“可用韩国 IP”，**不保证 Google 一定可达**。",
            "- `节点选择` 默认先给你 `KR-安全自动测速`，再给 `KR-全量自动测速`。",
            "- 免费代理波动很大，建议用前再执行一次刷新脚本。",
            "",
        ]
    )
    return "\n".join(lines)


def render_empty_yaml(generated_at: str) -> str:
    lines = [
        f"# Generated at {generated_at}",
        f"# Verified through {TEST_URL_HTTP} and {TEST_URL_HTTPS}",
        "# No KR proxy passed this round of KR + Naver validation.",
        "mixed-port: 7890",
        "allow-lan: false",
        "mode: rule",
        "log-level: info",
        "",
        "proxies: []",
        "",
        "proxy-groups:",
        "  - name: \"节点选择\"",
        "    type: select",
        "    proxies:",
        "      - DIRECT",
        "",
        "rules:",
        "  - MATCH,节点选择",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh KR proxies for Stash")
    parser.add_argument("--min-working", type=int, default=4, help="fallback to generic lists if fewer than this many working proxies")
    parser.add_argument("--monosans-limit", type=int, default=120, help="how many generic HTTP/SOCKS5 entries to test per monosans list when fallback is needed")
    parser.add_argument("--skillter-limit", type=int, default=120, help="how many generic HTTP/SOCKS5 entries to test per skillter list when fallback is needed")
    parser.add_argument("--workers", type=int, default=12, help="concurrent validator workers")
    args = parser.parse_args()

    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")

    all_candidates: list[Candidate] = []
    per_source_counts: dict[str, int] = {}

    for name, fn in (
        ("proxyscrape", fetch_proxyscrape),
        ("proxifly", fetch_proxifly),
        ("iplocate", fetch_iplocate),
        ("geonode", fetch_geonode),
        ("niek", fetch_niek),
        ("monosans_kr_json", fetch_monosans_kr_json),
    ):
        try:
            items = fn()
        except Exception as exc:
            items = []
            per_source_counts[f"{name}_error"] = 0
            (WORK / f"{name}_error.txt").write_text(str(exc), encoding="utf-8")
        per_source_counts[name] = len(items)
        all_candidates.extend(items)

    candidates = dedupe(all_candidates)

    results: list[Result] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(validate_candidate, item) for item in candidates]
        for fut in as_completed(futures):
            results.append(fut.result())

    working = [r for r in results if r.https_ok]

    if len(working) < args.min_working:
        fallback_all: list[Candidate] = []
        for name, fn in (
            ("monosans_fallback", lambda: fetch_monosans(limit=args.monosans_limit)),
            ("skillter_fallback", lambda: fetch_skillter(limit=args.skillter_limit)),
        ):
            try:
                items = fn()
            except Exception as exc:
                items = []
                (WORK / f"{name}_error.txt").write_text(str(exc), encoding="utf-8")
            per_source_counts[name] = len(items)
            fallback_all.extend(items)
        fallback_candidates = dedupe(fallback_all)
        seen = {(c.protocol, c.ip, c.port) for c in candidates}
        fallback_candidates = [c for c in fallback_candidates if (c.protocol, c.ip, c.port) not in seen]
        if fallback_candidates:
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                futures = [pool.submit(validate_candidate, item) for item in fallback_candidates]
                for fut in as_completed(futures):
                    results.append(fut.result())
            working = [r for r in results if r.https_ok]
    else:
        per_source_counts["monosans_fallback"] = 0
        per_source_counts["skillter_fallback"] = 0

    results = sort_results(results)
    working = sort_results([r for r in results if r.https_ok])

    snapshot = {
        "generated_at": generated_at,
        "per_source_counts": per_source_counts,
        "candidate_count_after_dedupe": len(dedupe(Candidate(**asdict(c)) for c in all_candidates)) if all_candidates else 0,
        "results": [asdict(r) for r in results],
    }
    (WORK / "tested_kr_proxies.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")

    if not working:
        yaml_text = render_empty_yaml(generated_at)
        (ROOT / "stash_kr_free.yaml").write_text(yaml_text, encoding="utf-8")
        report_text = render_report(generated_at, per_source_counts, len(candidates), working)
        (WORK / "source_report.md").write_text(report_text, encoding="utf-8")
        (WORK / "run_summary.json").write_text(
            json.dumps(
                {
                    "generated_at": generated_at,
                    "working_count": 0,
                    "message": "No KR proxy passed both geo and Naver HTTPS validation.",
                    "output_yaml": str(ROOT / "stash_kr_free.yaml"),
                    "tested_results": str(WORK / "tested_kr_proxies.json"),
                    "report": str(WORK / "source_report.md"),
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        return 0

    yaml_text = render_yaml(working, generated_at)
    (ROOT / "stash_kr_free.yaml").write_text(yaml_text, encoding="utf-8")

    report_text = render_report(generated_at, per_source_counts, len(candidates), working)
    (WORK / "source_report.md").write_text(report_text, encoding="utf-8")

    summary = {
        "generated_at": generated_at,
        "working_count": len(working),
        "working": [asdict(r) for r in working],
        "output_yaml": str(ROOT / "stash_kr_free.yaml"),
        "tested_results": str(WORK / "tested_kr_proxies.json"),
        "report": str(WORK / "source_report.md"),
    }
    (WORK / "run_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
