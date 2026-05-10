# KR 免费代理自动刷新报告（2026-05-10T15:10:09+00:00）

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

- geonode: 84
- iplocate: 1
- monosans_fallback: 0
- monosans_kr_json: 18
- niek: 18
- proxifly: 27
- proxyscrape: 86
- skillter_fallback: 0
- 去重后总候选: 194

## 当前验证通过的代理

- 1. `socks5://193.122.105.251:65535` | `socks5` | `elite` | 200 0.975280 | source=`geonode`
- 2. `socks5://121.169.46.116:1090` | `socks5` | `elite` | 200 0.999624 | source=`geonode`
- 3. `socks5://158.247.206.191:1080` | `socks5` | `elite` | 200 1.159590 | source=`proxyscrape`
- 4. `socks5://152.70.237.238:3128` | `socks5` | `elite` | 200 1.364895 | source=`proxyscrape`
- 5. `socks5://158.247.193.221:1080` | `socks5` | `elite` | 200 1.509761 | source=`proxyscrape`
- 6. `socks5://158.247.241.3:1080` | `socks5` | `elite` | 200 1.621484 | source=`proxyscrape`
- 7. `socks5://27.102.134.30:1082` | `socks5` | `elite` | 200 2.419066 | source=`proxyscrape`
- 8. `socks5://158.247.212.189:1080` | `socks5` | `elite` | 200 3.915183 | source=`proxyscrape`
- 9. `http://27.102.134.30:1082` | `http` | `elite` | 200 3.256564 | source=`proxyscrape`
- 10. `http://27.102.134.32:1082` | `http` | `elite` | 200 3.737118 | source=`proxyscrape`
- 11. `http://27.102.134.32:1081` | `http` | `elite` | 200 4.464472 | source=`proxyscrape`
- 12. `socks4://130.162.141.185:52916` | `socks4` | `elite` | 200 0.779119 | source=`proxyscrape`
- 13. `socks4://158.247.206.191:1080` | `socks4` | `elite` | 200 0.975127 | source=`proxyscrape`
- 14. `socks4://158.247.193.221:1080` | `socks4` | `elite` | 200 1.384819 | source=`proxyscrape`
- 15. `socks4://158.247.241.3:1080` | `socks4` | `elite` | 200 1.422404 | source=`proxyscrape`
- 16. `socks4://158.247.212.189:1080` | `socks4` | `elite` | 200 1.577505 | source=`proxyscrape`
- 17. `socks4://152.70.237.238:3128` | `socks4` | `elite` | 200 1.806045 | source=`proxyscrape`
- 18. `socks4://27.102.134.31:1082` | `socks4` | `elite` | 200 3.324538 | source=`proxyscrape`
- 19. `socks4://27.102.134.32:1082` | `socks4` | `elite` | 200 4.320331 | source=`proxyscrape`
- 20. `socks4://27.102.134.31:1081` | `socks4` | `elite` | 200 4.793748 | source=`proxyscrape`
- 21. `socks4://27.102.134.32:1081` | `socks4` | `elite` | 200 5.291473 | source=`proxyscrape`
- 22. `socks4://27.102.134.31:1080` | `socks4` | `elite` | 200 7.893486 | source=`proxyscrape`
- 23. `socks4://27.102.134.30:1080` | `socks4` | `elite` | 200 9.131995 | source=`proxyscrape`
- 24. `socks4://27.102.134.32:1080` | `socks4` | `elite` | 200 9.318887 | source=`proxyscrape`
- 25. `socks5://152.70.91.193:40000` | `socks5` | `unknown` | 200 1.675716 | source=`monosans_kr_json`
- 26. `socks5://27.102.134.32:1082` | `socks5` | `unknown` | 200 3.657938 | source=`monosans_kr_json`
- 27. `socks5://27.102.134.30:1090` | `socks5` | `unknown` | 200 4.597060 | source=`monosans_kr_json`
- 28. `socks5://27.102.134.32:1081` | `socks5` | `unknown` | 200 4.888361 | source=`monosans_kr_json`
- 29. `socks5://27.102.134.30:1080` | `socks5` | `unknown` | 200 7.444356 | source=`monosans_kr_json`
- 30. `socks5://27.102.134.31:1090` | `socks5` | `unknown` | 200 7.913172 | source=`monosans_kr_json`
- 31. `socks5://27.102.134.32:1080` | `socks5` | `unknown` | 200 9.498330 | source=`monosans_kr_json`
- 32. `socks5://27.102.134.30:1081` | `socks5` | `unknown` | 200 9.904606 | source=`monosans_kr_json`
- 33. `http://1.231.81.166:3128` | `http` | `unknown` | 200 0.996129 | source=`monosans_kr_json`
- 34. `http://27.102.134.31:1082` | `http` | `unknown` | 200 3.985657 | source=`monosans_kr_json`
- 35. `http://27.102.134.31:1081` | `http` | `unknown` | 200 4.238250 | source=`monosans_kr_json`
- 36. `http://27.102.134.31:1080` | `http` | `unknown` | 200 6.496691 | source=`monosans_kr_json`
- 37. `http://27.102.134.30:1080` | `http` | `unknown` | 200 7.734680 | source=`monosans_kr_json`
- 38. `http://27.102.134.31:1090` | `http` | `unknown` | 200 7.789919 | source=`monosans_kr_json`
- 39. `http://27.102.134.30:1081` | `http` | `unknown` | 200 7.933281 | source=`monosans_kr_json`
- 40. `socks5://158.179.173.238:1080` | `socks5` | `transparent` | 200 1.034663 | source=`proxifly`
- 41. `socks5://27.102.134.31:1082` | `socks5` | `transparent` | 200 2.867394 | source=`proxifly`
- 42. `socks5://27.102.134.31:1081` | `socks5` | `transparent` | 200 4.420171 | source=`proxifly`
- 43. `socks5://27.102.134.31:1080` | `socks5` | `transparent` | 200 6.357642 | source=`proxifly`
- 44. `http://220.121.143.33:3128` | `http` | `transparent` | 200 0.762151 | source=`proxifly`
- 45. `http://146.56.182.165:3128` | `http` | `transparent` | 200 0.795194 | source=`proxyscrape`
- 46. `socks4://27.102.134.30:1082` | `socks4` | `transparent` | 200 2.113462 | source=`proxifly`
- 47. `socks4://27.102.134.30:1090` | `socks4` | `transparent` | 200 4.949119 | source=`proxifly`
- 48. `socks4://27.102.134.30:1081` | `socks4` | `transparent` | 200 9.384918 | source=`proxifly`

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
