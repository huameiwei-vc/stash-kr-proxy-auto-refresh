# KR 免费代理自动刷新报告（2026-06-15T23:59:11+00:00）

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

- geonode: 103
- iplocate: 2
- monosans_fallback: 0
- monosans_kr_json: 10
- niek: 15
- proxifly: 20
- proxyscrape: 39
- skillter_fallback: 0
- 去重后总候选: 179

## 当前验证通过的代理

- 1. `socks5://121.169.46.116:1090` | `socks5` | `elite` | 200 0.850008 | source=`geonode`
- 2. `socks5://158.179.173.238:1080` | `socks5` | `elite` | 200 2.092988 | source=`proxyscrape`
- 3. `socks5://152.70.237.238:3128` | `socks5` | `elite` | 200 4.391237 | source=`geonode`
- 4. `socks4://211.245.23.166:1080` | `socks4` | `elite` | 200 0.650718 | source=`proxyscrape`
- 5. `socks4://152.70.237.238:3128` | `socks4` | `elite` | 200 4.203384 | source=`proxyscrape`
- 6. `socks5://211.245.23.166:1080` | `socks5` | `unknown` | 200 1.428235 | source=`monosans_kr_json`
- 7. `http://169.212.15.161:5000` | `http` | `unknown` | 200 3.618622 | source=`monosans_kr_json`
- 8. `http://43.155.132.199:3128` | `http` | `unknown` | 200 5.591396 | source=`monosans_kr_json`
- 9. `socks5://206.123.156.218:9533` | `socks5` | `transparent` | 200 4.185658 | source=`proxifly`
- 10. `socks5://206.123.156.231:21000` | `socks5` | `transparent` | 200 4.596834 | source=`proxifly`
- 11. `socks5://206.123.156.211:13372` | `socks5` | `transparent` | 200 6.611832 | source=`proxifly`
- 12. `socks5://206.123.156.227:4286` | `socks5` | `transparent` | 200 7.044406 | source=`proxifly`
- 13. `socks5://206.123.156.210:7553` | `socks5` | `transparent` | 200 8.465036 | source=`proxifly`
- 14. `socks5://206.123.156.223:7508` | `socks5` | `transparent` | 200 10.034221 | source=`proxifly`
- 15. `http://106.10.55.212:1121` | `http` | `transparent` | 200 2.136389 | source=`proxyscrape`

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
