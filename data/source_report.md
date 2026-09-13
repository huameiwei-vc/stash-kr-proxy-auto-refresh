# KR 免费代理自动刷新报告（2026-09-13T06:05:26+00:00）

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

- geonode: 11
- iplocate: 3
- monosans_fallback: 0
- monosans_kr_json: 32
- niek: 12
- proxifly: 52
- proxyscrape: 63
- skillter_fallback: 0
- 去重后总候选: 113

## 当前验证通过的代理

- 1. `http://121.170.165.80:17878` | `http` | `elite` | 200 0.754724 | source=`proxyscrape`
- 2. `http://211.42.144.253:24336` | `http` | `elite` | 200 0.756108 | source=`proxyscrape`
- 3. `http://211.42.144.254:24709` | `http` | `elite` | 200 0.762155 | source=`proxyscrape`
- 4. `http://183.111.73.44:27468` | `http` | `elite` | 200 0.766426 | source=`proxyscrape`
- 5. `http://210.121.160.236:16976` | `http` | `elite` | 200 0.767150 | source=`proxyscrape`
- 6. `http://210.121.160.228:13484` | `http` | `elite` | 200 0.812415 | source=`proxyscrape`
- 7. `http://210.121.160.128:23963` | `http` | `elite` | 200 0.938910 | source=`proxyscrape`
- 8. `http://210.121.160.121:23731` | `http` | `elite` | 200 1.048946 | source=`proxyscrape`
- 9. `http://210.220.138.216:15398` | `http` | `elite` | 200 1.085453 | source=`proxyscrape`
- 10. `http://1.231.81.166:3128` | `http` | `unknown` | 200 0.755948 | source=`monosans_kr_json`
- 11. `http://210.121.160.230:15289` | `http` | `unknown` | 200 0.758622 | source=`monosans_kr_json`
- 12. `http://183.111.192.204:16940` | `http` | `unknown` | 200 0.765680 | source=`monosans_kr_json`
- 13. `http://121.170.165.58:22025` | `http` | `unknown` | 200 0.767645 | source=`monosans_kr_json`
- 14. `http://210.121.160.15:24967` | `http` | `unknown` | 200 0.770986 | source=`monosans_kr_json`
- 15. `http://121.170.165.68:25180` | `http` | `unknown` | 200 0.770771 | source=`monosans_kr_json`
- 16. `http://210.121.160.91:11590` | `http` | `unknown` | 200 0.772315 | source=`monosans_kr_json`
- 17. `http://210.121.160.86:12842` | `http` | `unknown` | 200 0.823766 | source=`monosans_kr_json`
- 18. `http://210.121.160.96:24659` | `http` | `unknown` | 200 0.844179 | source=`monosans_kr_json`
- 19. `http://210.121.160.114:17056` | `http` | `unknown` | 200 0.848425 | source=`monosans_kr_json`
- 20. `http://210.121.160.207:28276` | `http` | `unknown` | 200 0.871913 | source=`monosans_kr_json`
- 21. `http://210.121.160.79:28510` | `http` | `unknown` | 200 0.899981 | source=`monosans_kr_json`
- 22. `http://210.121.160.239:10943` | `http` | `unknown` | 200 0.912820 | source=`monosans_kr_json`
- 23. `http://121.170.165.76:24818` | `http` | `unknown` | 200 0.921842 | source=`monosans_kr_json`
- 24. `http://183.111.179.185:26123` | `http` | `unknown` | 200 0.947487 | source=`monosans_kr_json`
- 25. `http://121.170.165.85:13109` | `http` | `unknown` | 200 1.090598 | source=`monosans_kr_json`
- 26. `http://210.121.160.131:27336` | `http` | `unknown` | 200 1.388469 | source=`monosans_kr_json`
- 27. `http://210.121.160.141:12976` | `http` | `unknown` | 200 1.637216 | source=`monosans_kr_json`
- 28. `http://121.170.165.35:23446` | `http` | `unknown` | 200 1.645972 | source=`monosans_kr_json`
- 29. `http://203.245.16.114:19715` | `http` | `unknown` | 200 1.671903 | source=`monosans_kr_json`
- 30. `http://121.170.165.97:19797` | `http` | `unknown` | 200 1.885453 | source=`monosans_kr_json`
- 31. `http://210.121.160.105:25802` | `http` | `unknown` | 200 2.224353 | source=`monosans_kr_json`
- 32. `http://210.121.160.43:12410` | `http` | `unknown` | 200 2.224968 | source=`monosans_kr_json`
- 33. `http://203.245.16.113:27875` | `http` | `unknown` | 200 2.592005 | source=`monosans_kr_json`
- 34. `http://121.170.165.32:10127` | `http` | `unknown` | 200 3.068965 | source=`monosans_kr_json`
- 35. `http://210.121.160.187:20033` | `http` | `unknown` | 200 3.532958 | source=`monosans_kr_json`
- 36. `http://183.101.185.89:20002` | `http` | `unknown` | 200 4.825388 | source=`niek`
- 37. `http://210.121.160.226:26431` | `http` | `unknown` | 200 6.214050 | source=`monosans_kr_json`
- 38. `http://210.121.160.202:24100` | `http` | `unknown` | 200 6.403438 | source=`monosans_kr_json`
- 39. `http://211.63.212.230:15611` | `http` | `transparent` | 200 0.740314 | source=`proxifly`
- 40. `http://183.111.192.207:11338` | `http` | `transparent` | 200 0.761525 | source=`proxifly`
- 41. `http://210.121.160.83:14884` | `http` | `transparent` | 200 0.774278 | source=`proxifly`
- 42. `http://210.121.160.247:10264` | `http` | `transparent` | 200 0.847761 | source=`proxifly`
- 43. `http://210.121.160.8:11358` | `http` | `transparent` | 200 0.914786 | source=`proxifly`
- 44. `http://121.170.165.243:28754` | `http` | `transparent` | 200 1.081776 | source=`proxifly`
- 45. `http://210.121.160.157:25341` | `http` | `transparent` | 200 1.272683 | source=`proxifly`
- 46. `http://210.121.160.170:23904` | `http` | `transparent` | 200 2.252392 | source=`proxifly`
- 47. `http://210.121.160.217:29454` | `http` | `transparent` | 200 2.463463 | source=`proxifly`
- 48. `http://121.170.165.29:10676` | `http` | `transparent` | 200 2.553517 | source=`proxifly`
- 49. `http://121.170.165.27:21833` | `http` | `transparent` | 200 2.637448 | source=`proxifly`
- 50. `http://211.217.231.234:8080` | `http` | `transparent` | 200 4.030988 | source=`proxifly`
- 51. `http://121.170.165.3:24439` | `http` | `transparent` | 200 4.374301 | source=`proxifly`
- 52. `http://210.121.160.108:18986` | `http` | `transparent` | 200 6.443063 | source=`proxifly`
- 53. `http://210.121.160.42:18181` | `http` | `transparent` | 200 6.755866 | source=`proxifly`

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
