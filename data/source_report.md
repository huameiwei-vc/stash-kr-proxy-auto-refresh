# KR 免费代理自动刷新报告（2026-05-10T16:05:55+00:00）

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

- geonode: 87
- iplocate: 1
- monosans_fallback: 0
- monosans_kr_json: 23
- niek: 18
- proxifly: 24
- proxyscrape: 84
- skillter_fallback: 0
- 去重后总候选: 195

## 当前验证通过的代理

- 1. `socks5://121.169.46.116:1090` | `socks5` | `elite` | 200 0.946950 | source=`geonode`
- 2. `socks5://146.56.185.39:10800` | `socks5` | `elite` | 200 1.413740 | source=`proxyscrape`
- 3. `socks5://152.70.91.193:40000` | `socks5` | `elite` | 200 1.514885 | source=`geonode`
- 4. `socks5://27.102.134.30:1081` | `socks5` | `elite` | 200 6.532603 | source=`proxyscrape`
- 5. `socks4://146.56.185.39:10800` | `socks4` | `elite` | 200 1.161167 | source=`proxyscrape`
- 6. `socks4://158.247.206.191:1080` | `socks4` | `elite` | 200 2.285699 | source=`proxyscrape`
- 7. `socks4://130.162.141.185:52916` | `socks4` | `elite` | 200 3.262337 | source=`proxyscrape`
- 8. `socks4://27.102.134.31:1081` | `socks4` | `elite` | 200 4.752688 | source=`proxyscrape`
- 9. `socks4://27.102.134.32:1081` | `socks4` | `elite` | 200 5.547405 | source=`proxyscrape`
- 10. `socks4://27.102.134.31:1082` | `socks4` | `elite` | 200 6.387212 | source=`proxyscrape`
- 11. `socks4://27.102.134.31:1080` | `socks4` | `elite` | 200 6.596284 | source=`proxyscrape`
- 12. `socks4://27.102.134.30:1090` | `socks4` | `elite` | 200 6.608490 | source=`proxyscrape`
- 13. `socks4://27.102.134.30:1080` | `socks4` | `elite` | 200 6.685478 | source=`proxyscrape`
- 14. `socks4://27.102.134.32:1080` | `socks4` | `elite` | 200 7.920865 | source=`proxyscrape`
- 15. `socks4://27.102.134.32:1082` | `socks4` | `elite` | 200 9.897104 | source=`proxyscrape`
- 16. `socks4://27.102.134.31:1090` | `socks4` | `elite` | 200 11.137559 | source=`proxyscrape`
- 17. `http://210.223.44.230:3128` | `http` | `anonymous` | 200 2.588520 | source=`proxyscrape`
- 18. `socks5://27.102.134.30:1080` | `socks5` | `unknown` | 200 4.973420 | source=`monosans_kr_json`
- 19. `socks5://27.102.134.31:1081` | `socks5` | `unknown` | 200 5.320959 | source=`monosans_kr_json`
- 20. `socks5://27.102.134.30:1082` | `socks5` | `unknown` | 200 5.548648 | source=`monosans_kr_json`
- 21. `socks5://27.102.134.31:1082` | `socks5` | `unknown` | 200 6.749613 | source=`monosans_kr_json`
- 22. `socks5://27.102.134.31:1080` | `socks5` | `unknown` | 200 6.757188 | source=`monosans_kr_json`
- 23. `socks5://27.102.134.32:1080` | `socks5` | `unknown` | 200 6.893213 | source=`monosans_kr_json`
- 24. `socks5://27.102.134.30:1090` | `socks5` | `unknown` | 200 9.156050 | source=`monosans_kr_json`
- 25. `socks5://27.102.134.31:1090` | `socks5` | `unknown` | 200 10.073664 | source=`monosans_kr_json`
- 26. `socks5://27.102.134.32:1082` | `socks5` | `unknown` | 200 11.850097 | source=`monosans_kr_json`
- 27. `http://1.231.81.166:3128` | `http` | `unknown` | 200 0.896813 | source=`monosans_kr_json`
- 28. `http://27.102.134.31:1080` | `http` | `unknown` | 200 5.620297 | source=`monosans_kr_json`
- 29. `http://27.102.134.31:1082` | `http` | `unknown` | 200 5.659767 | source=`monosans_kr_json`
- 30. `http://27.102.134.31:1081` | `http` | `unknown` | 200 6.023365 | source=`monosans_kr_json`
- 31. `http://27.102.134.30:1082` | `http` | `unknown` | 200 6.057622 | source=`monosans_kr_json`
- 32. `http://27.102.134.32:1081` | `http` | `unknown` | 200 6.203661 | source=`monosans_kr_json`
- 33. `http://27.102.134.30:1081` | `http` | `unknown` | 200 6.584046 | source=`monosans_kr_json`
- 34. `http://27.102.134.30:1080` | `http` | `unknown` | 200 7.596362 | source=`monosans_kr_json`
- 35. `http://27.102.134.32:1080` | `http` | `unknown` | 200 8.155080 | source=`monosans_kr_json`
- 36. `http://27.102.134.30:1090` | `http` | `unknown` | 200 9.052415 | source=`monosans_kr_json`
- 37. `http://27.102.134.32:1082` | `http` | `unknown` | 200 10.334494 | source=`monosans_kr_json`
- 38. `socks4://27.102.134.30:1082` | `socks4` | `transparent` | 200 5.986748 | source=`proxifly`
- 39. `socks4://27.102.134.30:1081` | `socks4` | `transparent` | 200 6.245639 | source=`proxifly`

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
