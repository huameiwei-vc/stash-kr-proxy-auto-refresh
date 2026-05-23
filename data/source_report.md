# KR 免费代理自动刷新报告（2026-05-23T07:24:07+00:00）

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

- geonode: 101
- iplocate: 11
- monosans_fallback: 0
- monosans_kr_json: 5
- niek: 10
- proxifly: 18
- proxyscrape: 51
- skillter_fallback: 0
- 去重后总候选: 184

## 当前验证通过的代理

- 1. `socks5://121.169.46.116:1090` | `socks5` | `elite` | 200 2.714141 | source=`geonode`
- 2. `http://3.38.161.46:1080` | `http` | `elite` | 200 0.801757 | source=`proxyscrape`
- 3. `http://3.38.206.96:1080` | `http` | `elite` | 200 0.867532 | source=`proxyscrape`
- 4. `http://43.203.112.93:1080` | `http` | `elite` | 200 0.885167 | source=`proxyscrape`
- 5. `http://43.201.153.78:1080` | `http` | `elite` | 200 0.949886 | source=`proxyscrape`
- 6. `http://3.38.172.68:1080` | `http` | `elite` | 200 1.385196 | source=`proxyscrape`
- 7. `http://43.201.153.25:1080` | `http` | `elite` | 200 2.194672 | source=`proxyscrape`
- 8. `http://43.203.117.104:1080` | `http` | `elite` | 200 2.752723 | source=`proxyscrape`
- 9. `http://3.38.198.134:1080` | `http` | `elite` | 200 3.094220 | source=`proxyscrape`
- 10. `http://3.38.146.139:1080` | `http` | `elite` | 200 3.217905 | source=`proxyscrape`
- 11. `http://43.203.112.144:1080` | `http` | `elite` | 200 3.255986 | source=`proxyscrape`
- 12. `http://43.201.153.87:1080` | `http` | `elite` | 200 4.562778 | source=`proxyscrape`
- 13. `http://3.38.163.43:1080` | `http` | `elite` | 200 6.091265 | source=`proxyscrape`
- 14. `http://43.201.153.223:1080` | `http` | `elite` | 200 6.222965 | source=`proxyscrape`
- 15. `http://3.38.194.119:1080` | `http` | `elite` | 200 10.284245 | source=`proxyscrape`
- 16. `socks4://144.24.84.140:7890` | `socks4` | `elite` | 200 1.666393 | source=`proxyscrape`
- 17. `http://3.38.167.255:1080` | `http` | `unknown` | 200 0.889952 | source=`monosans_kr_json`
- 18. `http://1.231.81.166:3128` | `http` | `unknown` | 200 1.002003 | source=`monosans_kr_json`
- 19. `http://144.24.84.140:7890` | `http` | `unknown` | 200 1.006139 | source=`niek`

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
