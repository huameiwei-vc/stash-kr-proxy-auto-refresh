# KR 免费代理自动刷新报告（2026-09-13T11:44:11+00:00）

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

- geonode: 12
- iplocate: 3
- monosans_fallback: 0
- monosans_kr_json: 11
- niek: 12
- proxifly: 41
- proxyscrape: 33
- skillter_fallback: 0
- 去重后总候选: 97

## 当前验证通过的代理

- 1. `http://210.121.160.223:19059` | `http` | `elite` | 200 2.790159 | source=`proxyscrape`
- 2. `http://183.111.73.44:27468` | `http` | `elite` | 200 3.666197 | source=`proxyscrape`
- 3. `http://210.121.160.189:29154` | `http` | `elite` | 200 3.740029 | source=`proxyscrape`
- 4. `http://210.121.160.118:29694` | `http` | `elite` | 200 4.660544 | source=`proxyscrape`
- 5. `http://121.170.165.32:10127` | `http` | `elite` | 200 6.028897 | source=`proxyscrape`
- 6. `http://1.231.81.166:3128` | `http` | `unknown` | 200 0.568668 | source=`monosans_kr_json`
- 7. `http://210.121.160.128:23963` | `http` | `unknown` | 200 1.082806 | source=`monosans_kr_json`
- 8. `http://121.170.165.39:25448` | `http` | `unknown` | 200 1.238573 | source=`monosans_kr_json`
- 9. `http://210.121.160.92:13978` | `http` | `unknown` | 200 1.273418 | source=`monosans_kr_json`
- 10. `http://121.170.165.68:25180` | `http` | `unknown` | 200 1.315840 | source=`monosans_kr_json`
- 11. `http://210.121.160.115:21832` | `http` | `unknown` | 200 1.323890 | source=`monosans_kr_json`
- 12. `http://210.121.160.91:11590` | `http` | `unknown` | 200 1.370976 | source=`monosans_kr_json`
- 13. `http://210.121.160.79:28510` | `http` | `unknown` | 200 1.423000 | source=`monosans_kr_json`
- 14. `http://210.121.160.230:15289` | `http` | `unknown` | 200 1.443628 | source=`monosans_kr_json`
- 15. `http://210.121.160.168:20209` | `http` | `unknown` | 200 3.590028 | source=`monosans_kr_json`
- 16. `http://210.121.160.228:13484` | `http` | `unknown` | 200 8.865120 | source=`monosans_kr_json`
- 17. `socks5://121.169.46.116:1090` | `socks5` | `transparent` | 200 1.199194 | source=`proxifly`
- 18. `http://210.121.160.13:26440` | `http` | `transparent` | 200 1.692796 | source=`proxifly`
- 19. `http://121.170.165.38:17548` | `http` | `transparent` | 200 1.914562 | source=`proxifly`
- 20. `http://210.121.160.217:29454` | `http` | `transparent` | 200 3.379478 | source=`proxifly`
- 21. `http://210.121.160.129:27017` | `http` | `transparent` | 200 3.556547 | source=`proxifly`
- 22. `http://183.111.192.207:11338` | `http` | `transparent` | 200 3.883570 | source=`proxifly`
- 23. `http://210.121.160.8:11358` | `http` | `transparent` | 200 4.092945 | source=`proxifly`
- 24. `http://210.121.160.239:10943` | `http` | `transparent` | 200 4.261397 | source=`proxifly`
- 25. `http://121.170.165.243:28754` | `http` | `transparent` | 200 4.312545 | source=`proxifly`
- 26. `http://210.121.160.43:12410` | `http` | `transparent` | 200 4.392465 | source=`proxifly`
- 27. `http://210.121.160.15:24967` | `http` | `transparent` | 200 4.550612 | source=`proxifly`
- 28. `http://210.121.160.121:23731` | `http` | `transparent` | 200 4.603819 | source=`proxifly`
- 29. `http://210.121.160.137:17175` | `http` | `transparent` | 200 5.270426 | source=`proxifly`
- 30. `http://211.42.144.254:24709` | `http` | `transparent` | 200 5.585549 | source=`proxifly`
- 31. `http://210.121.160.153:15903` | `http` | `transparent` | 200 7.491223 | source=`proxifly`
- 32. `http://210.121.160.236:16976` | `http` | `transparent` | 200 7.641378 | source=`proxifly`
- 33. `http://210.220.138.217:16051` | `http` | `transparent` | 200 8.559238 | source=`proxifly`
- 34. `http://210.121.160.44:26719` | `http` | `transparent` | 200 9.282694 | source=`proxifly`
- 35. `http://203.245.16.114:19715` | `http` | `transparent` | 200 9.586704 | source=`proxifly`
- 36. `http://210.121.160.141:12976` | `http` | `transparent` | 200 10.339326 | source=`proxifly`
- 37. `http://210.121.160.202:24100` | `http` | `transparent` | 200 11.429443 | source=`proxifly`
- 38. `http://211.63.212.230:15611` | `http` | `transparent` | 200 11.490737 | source=`proxifly`

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
