# KR 免费代理自动刷新报告（2026-06-03T22:23:37+00:00）

> 目标：自动抓取并验证当前可用于 Stash 的韩国代理，仅在当前目录生成结果。

## 采用的自动化来源

1. **ProxyScrape 官方 API**  
   - <https://api.proxyscrape.com/v4/free-proxy-list/get?request=get_proxies&country=KR&proxy_format=protocolipport&format=json&skip=0&limit=100>
2. **Proxifly 韩国国家列表**  
   - <https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/countries/KR/data.json>
3. **iplocate 韩国国家列表**  
   - <https://raw.githubusercontent.com/iplocate/free-proxy-list/main/countries/KR/proxies.txt>
4. **Geonode 韩国代理 API**  
   - <https://proxylist.geonode.com/api/proxy-list?limit=200&page=1&sort_by=lastChecked&sort_type=desc&country=KR>
5. **niek 实时页面**  
   - <https://niek.github.io/free-proxy-list/>
6. **monosans 带地理信息的 KR 列表**  
   - <https://raw.githubusercontent.com/monosans/proxy-list/main/proxies.json>
7. **通用列表兜底（仅在 KR 专用来源不足时测试）**  
   - <https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt>  
   - <https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt>  
   - <https://raw.githubusercontent.com/Skillter/ProxyGather/master/proxies/working-proxies-http.txt>  
   - <https://raw.githubusercontent.com/Skillter/ProxyGather/master/proxies/working-proxies-socks5.txt>

## 原始候选数量

- geonode: 110
- iplocate: 2
- monosans_fallback: 0
- monosans_kr_json: 5
- niek: 13
- proxifly: 11
- proxyscrape: 38
- skillter_fallback: 0
- 去重后总候选: 164

## 当前验证通过的代理

- 1. `socks5://118.36.249.175:2080` | `socks5` | `elite` | 200 0.955495 | source=`proxyscrape`
- 2. `socks5://121.169.46.116:1090` | `socks5` | `elite` | 200 1.167202 | source=`geonode`
- 3. `socks5://158.180.77.24:1080` | `socks5` | `elite` | 200 1.213341 | source=`geonode`
- 4. `http://203.232.107.6:2080` | `http` | `elite` | 200 0.552841 | source=`proxyscrape`
- 5. `http://210.223.44.230:3128` | `http` | `anonymous` | 200 1.677753 | source=`proxyscrape`
- 6. `socks5://150.230.249.50:1080` | `socks5` | `unknown` | 200 1.712598 | source=`monosans_kr_json`
- 7. `http://150.230.249.50:1080` | `http` | `unknown` | 200 0.560179 | source=`niek`
- 8. `http://175.198.235.18:3128` | `http` | `unknown` | 200 0.566681 | source=`monosans_kr_json`
- 9. `http://43.128.145.26:1080` | `http` | `unknown` | 200 0.837218 | source=`monosans_kr_json`
- 10. `http://1.231.81.166:3128` | `http` | `unknown` | 200 3.045320 | source=`monosans_kr_json`
- 11. `socks5://203.232.107.6:2080` | `socks5` | `transparent` | 200 0.695075 | source=`proxifly`

## 输出文件

- Stash 配置：`/home/runner/work/stash-kr-proxy-auto-refresh/stash-kr-proxy-auto-refresh/stash_kr_free.yaml`
- 测试明细：`/home/runner/work/stash-kr-proxy-auto-refresh/stash-kr-proxy-auto-refresh/data/tested_kr_proxies.json`
- 运行摘要：`/home/runner/work/stash-kr-proxy-auto-refresh/stash-kr-proxy-auto-refresh/data/run_summary.json`
- 本脚本：`/home/runner/work/stash-kr-proxy-auto-refresh/stash-kr-proxy-auto-refresh/data/refresh_kr_stash.py`

## 说明

- 只保留同时满足 **KR 出口** 和 **Naver HTTPS 可连** 的代理。
- 当前配置的用途是“可用韩国 IP”，**不保证 Google 一定可达**。
- `节点选择` 默认先给你 `KR-安全自动测速`，再给 `KR-全量自动测速`。
- 免费代理波动很大，建议用前再执行一次刷新脚本。
