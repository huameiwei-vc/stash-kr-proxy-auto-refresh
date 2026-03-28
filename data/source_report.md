# KR 免费代理自动刷新报告（2026-03-28T12:21:32+00:00）

> 目标：自动抓取并验证当前可用于 Stash 的韩国代理，仅在当前目录生成结果。

## 采用的自动化来源

1. **ProxyScrape 官方 API**  
   - <https://api.proxyscrape.com/v4/free-proxy-list/get?request=get_proxies&country=KR&proxy_format=protocolipport&format=json&skip=0&limit=100>
2. **Proxifly 韩国国家列表**  
   - <https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/countries/KR/data.json>
3. **iplocate 韩国国家列表**  
   - <https://raw.githubusercontent.com/iplocate/free-proxy-list/main/countries/KR/proxies.txt>
4. **monosans 通用列表（仅在前述来源不足时作为网络搜索后的兜底）**  
   - <https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt>  
   - <https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt>

## 原始候选数量

- iplocate: 1
- monosans_fallback: 184
- proxifly: 9
- proxyscrape: 21
- 去重后总候选: 29

## 当前验证通过的代理

- 1. `socks5://94.130.16.48:30006` | `socks5` | `unknown` | 204 6.327540 | source=`monosans_socks5`
- 2. `http://121.126.185.63:25152` | `http` | `unknown` | 204 5.773133 | source=`iplocate`
- 3. `http://1.231.81.166:3128` | `http` | `transparent` | 204 0.891773 | source=`proxyscrape`

## 输出文件

- Stash 配置：`/home/runner/work/stash-kr-proxy-auto-refresh/stash-kr-proxy-auto-refresh/stash_kr_free.yaml`
- 测试明细：`/home/runner/work/stash-kr-proxy-auto-refresh/stash-kr-proxy-auto-refresh/data/tested_kr_proxies.json`
- 运行摘要：`/home/runner/work/stash-kr-proxy-auto-refresh/stash-kr-proxy-auto-refresh/data/run_summary.json`
- 本脚本：`/home/runner/work/stash-kr-proxy-auto-refresh/stash-kr-proxy-auto-refresh/data/refresh_kr_stash.py`

## 说明

- 只保留同时满足 **KR 出口** 和 **HTTPS 可连** 的代理。
- `节点选择` 默认先给你 `KR-安全自动测速`，再给 `KR-全量自动测速`。
- 免费代理波动很大，建议用前再执行一次刷新脚本。
