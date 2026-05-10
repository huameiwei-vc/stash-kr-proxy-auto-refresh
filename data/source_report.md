# KR 免费代理自动刷新报告（2026-05-10T23:04:18+00:00）

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

- geonode: 90
- iplocate: 2
- monosans_fallback: 0
- monosans_kr_json: 6
- niek: 18
- proxifly: 15
- proxyscrape: 67
- skillter_fallback: 0
- 去重后总候选: 181

## 当前验证通过的代理

- 1. `socks5://121.169.46.116:1090` | `socks5` | `elite` | 200 1.110211 | source=`geonode`
- 2. `socks5://27.102.134.30:1081` | `socks5` | `elite` | 200 3.581073 | source=`proxyscrape`
- 3. `socks5://27.102.134.30:1090` | `socks5` | `elite` | 200 3.583008 | source=`proxyscrape`
- 4. `socks5://27.102.134.30:1082` | `socks5` | `elite` | 200 3.598669 | source=`proxyscrape`
- 5. `socks5://27.102.134.32:1080` | `socks5` | `elite` | 200 4.607692 | source=`proxyscrape`
- 6. `socks5://27.102.134.31:1090` | `socks5` | `elite` | 200 4.672973 | source=`proxyscrape`
- 7. `http://27.102.134.30:1082` | `http` | `elite` | 200 2.482219 | source=`proxyscrape`
- 8. `http://27.102.134.32:1082` | `http` | `elite` | 200 2.649076 | source=`proxyscrape`
- 9. `http://27.102.134.31:1082` | `http` | `elite` | 200 4.017881 | source=`proxyscrape`
- 10. `http://27.102.134.32:1080` | `http` | `elite` | 200 4.328532 | source=`proxyscrape`
- 11. `http://27.102.134.30:1080` | `http` | `elite` | 200 5.333211 | source=`proxyscrape`
- 12. `http://27.102.134.32:1081` | `http` | `elite` | 200 7.716911 | source=`proxyscrape`
- 13. `http://27.102.134.31:1080` | `http` | `elite` | 200 7.941197 | source=`proxyscrape`
- 14. `socks4://27.102.134.30:1082` | `socks4` | `elite` | 200 2.633177 | source=`proxyscrape`
- 15. `socks4://27.102.134.32:1082` | `socks4` | `elite` | 200 2.832694 | source=`proxyscrape`
- 16. `socks4://27.102.134.30:1090` | `socks4` | `elite` | 200 3.025658 | source=`proxyscrape`
- 17. `socks4://27.102.134.30:1081` | `socks4` | `elite` | 200 3.306400 | source=`proxyscrape`
- 18. `socks4://27.102.134.31:1081` | `socks4` | `elite` | 200 3.949607 | source=`proxyscrape`
- 19. `socks4://27.102.134.31:1082` | `socks4` | `elite` | 200 3.972365 | source=`proxyscrape`
- 20. `socks4://27.102.134.31:1090` | `socks4` | `elite` | 200 4.179017 | source=`proxyscrape`
- 21. `socks4://27.102.134.32:1080` | `socks4` | `elite` | 200 4.526048 | source=`proxyscrape`
- 22. `socks4://27.102.134.30:1080` | `socks4` | `elite` | 200 5.700738 | source=`proxyscrape`
- 23. `socks4://27.102.134.32:1081` | `socks4` | `elite` | 200 6.786575 | source=`proxyscrape`
- 24. `socks4://27.102.134.31:1080` | `socks4` | `elite` | 200 7.977226 | source=`proxyscrape`
- 25. `socks5://27.102.134.31:1080` | `socks5` | `unknown` | 200 9.185558 | source=`monosans_kr_json`
- 26. `http://1.231.81.166:3128` | `http` | `unknown` | 200 0.966557 | source=`monosans_kr_json`
- 27. `http://27.102.134.30:1090` | `http` | `unknown` | 200 2.806480 | source=`monosans_kr_json`
- 28. `http://27.102.134.31:1081` | `http` | `unknown` | 200 3.921057 | source=`monosans_kr_json`
- 29. `http://27.102.134.30:1081` | `http` | `unknown` | 200 4.197826 | source=`niek`
- 30. `http://27.102.134.31:1090` | `http` | `unknown` | 200 4.481038 | source=`niek`
- 31. `socks5://27.102.134.31:1081` | `socks5` | `transparent` | 200 3.707544 | source=`proxifly`
- 32. `socks5://27.102.134.31:1082` | `socks5` | `transparent` | 200 4.848051 | source=`proxifly`
- 33. `socks5://27.102.134.30:1080` | `socks5` | `transparent` | 200 8.697753 | source=`proxifly`

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
