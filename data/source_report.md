# KR 免费代理自动刷新报告（2026-04-09T21:56:02+00:00）

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

- geonode: 31
- iplocate: 1
- monosans_fallback: 0
- monosans_kr_json: 10
- niek: 5
- proxifly: 159
- proxyscrape: 17
- skillter_fallback: 0
- 去重后总候选: 213

## 当前验证通过的代理

- 1. `http://1.231.81.166:3128` | `http` | `unknown` | 200 0.916337 | source=`monosans_kr_json`
- 2. `http://121.130.199.80:3128` | `http` | `unknown` | 200 0.965369 | source=`iplocate`
- 3. `socks5://110.10.174.60:1080` | `socks5` | `transparent` | 200 0.840404 | source=`proxifly`
- 4. `socks5://121.169.46.116:1090` | `socks5` | `transparent` | 200 0.874387 | source=`proxifly`
- 5. `socks5://206.123.156.177:9161` | `socks5` | `transparent` | 200 3.076091 | source=`proxifly`
- 6. `socks5://206.123.156.178:9411` | `socks5` | `transparent` | 200 3.127611 | source=`proxifly`
- 7. `socks5://206.123.156.205:6868` | `socks5` | `transparent` | 200 3.220568 | source=`proxifly`
- 8. `socks5://206.123.156.232:8165` | `socks5` | `transparent` | 200 3.231085 | source=`proxifly`
- 9. `socks5://206.123.156.177:4632` | `socks5` | `transparent` | 200 3.820811 | source=`proxifly`
- 10. `socks5://206.123.156.212:6539` | `socks5` | `transparent` | 200 4.081073 | source=`proxifly`
- 11. `socks5://206.123.156.207:8388` | `socks5` | `transparent` | 200 4.231207 | source=`proxifly`
- 12. `socks5://206.123.156.238:4816` | `socks5` | `transparent` | 200 4.725051 | source=`proxifly`
- 13. `socks5://206.123.156.224:5622` | `socks5` | `transparent` | 200 4.913499 | source=`proxifly`
- 14. `socks5://206.123.156.189:7826` | `socks5` | `transparent` | 200 4.963949 | source=`proxifly`
- 15. `socks5://206.123.156.223:4716` | `socks5` | `transparent` | 200 4.972016 | source=`proxifly`
- 16. `socks5://206.123.156.190:4602` | `socks5` | `transparent` | 200 5.041538 | source=`proxifly`
- 17. `socks5://206.123.156.212:8400` | `socks5` | `transparent` | 200 5.437698 | source=`proxifly`
- 18. `socks5://206.123.156.204:4196` | `socks5` | `transparent` | 200 6.094879 | source=`proxifly`
- 19. `socks5://206.123.156.233:5748` | `socks5` | `transparent` | 200 6.245875 | source=`proxifly`
- 20. `socks5://206.123.156.226:4205` | `socks5` | `transparent` | 200 6.638513 | source=`proxifly`
- 21. `socks5://206.123.156.204:5729` | `socks5` | `transparent` | 200 7.511876 | source=`proxifly`
- 22. `socks5://206.123.156.226:4386` | `socks5` | `transparent` | 200 8.325001 | source=`proxifly`
- 23. `socks5://206.123.156.224:17169` | `socks5` | `transparent` | 200 9.098603 | source=`proxifly`
- 24. `socks5://206.123.156.185:7342` | `socks5` | `transparent` | 200 9.523290 | source=`proxifly`
- 25. `http://121.147.253.205:3012` | `http` | `transparent` | 200 4.604649 | source=`proxifly`
- 26. `http://221.152.58.131:3068` | `http` | `transparent` | 200 7.250485 | source=`proxifly`

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
