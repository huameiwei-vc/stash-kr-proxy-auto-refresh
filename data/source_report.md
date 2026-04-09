# KR 免费代理自动刷新报告（2026-04-09T03:26:08+00:00）

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

- geonode: 32
- iplocate: 2
- monosans_fallback: 0
- monosans_kr_json: 41
- niek: 5
- proxifly: 71
- proxyscrape: 16
- skillter_fallback: 0
- 去重后总候选: 133

## 当前验证通过的代理

- 1. `http://1.234.153.14:80` | `http` | `anonymous` | 200 0.749223 | source=`proxyscrape`
- 2. `socks5://110.10.174.60:1080` | `socks5` | `unknown` | 200 0.930036 | source=`monosans_kr_json`
- 3. `socks5://206.123.156.236:6426` | `socks5` | `unknown` | 200 3.118816 | source=`monosans_kr_json`
- 4. `socks5://206.123.156.191:6969` | `socks5` | `unknown` | 200 3.474569 | source=`monosans_kr_json`
- 5. `socks5://206.123.156.185:8298` | `socks5` | `unknown` | 200 3.911995 | source=`monosans_kr_json`
- 6. `socks5://206.123.156.205:6868` | `socks5` | `unknown` | 200 3.925307 | source=`monosans_kr_json`
- 7. `socks5://206.123.156.212:16040` | `socks5` | `unknown` | 200 4.048070 | source=`monosans_kr_json`
- 8. `socks5://206.123.156.182:5835` | `socks5` | `unknown` | 200 4.290637 | source=`monosans_kr_json`
- 9. `socks5://206.123.156.180:36010` | `socks5` | `unknown` | 200 4.358305 | source=`monosans_kr_json`
- 10. `socks5://206.123.156.191:8116` | `socks5` | `unknown` | 200 4.934785 | source=`monosans_kr_json`
- 11. `socks5://206.123.156.207:5401` | `socks5` | `unknown` | 200 6.825270 | source=`monosans_kr_json`
- 12. `socks5://206.123.156.196:4512` | `socks5` | `unknown` | 200 8.113919 | source=`iplocate`
- 13. `http://1.231.81.166:3128` | `http` | `unknown` | 200 1.135111 | source=`monosans_kr_json`
- 14. `socks5://121.169.46.116:1090` | `socks5` | `transparent` | 200 1.072546 | source=`proxifly`
- 15. `socks5://206.123.156.207:8954` | `socks5` | `transparent` | 200 3.052791 | source=`proxifly`
- 16. `socks5://206.123.156.222:9975` | `socks5` | `transparent` | 200 3.124431 | source=`proxifly`
- 17. `socks5://206.123.156.220:4136` | `socks5` | `transparent` | 200 3.303097 | source=`proxifly`
- 18. `socks5://206.123.156.238:7251` | `socks5` | `transparent` | 200 3.332455 | source=`proxifly`
- 19. `socks5://206.123.156.238:9448` | `socks5` | `transparent` | 200 3.479388 | source=`proxifly`
- 20. `socks5://206.123.156.204:9964` | `socks5` | `transparent` | 200 4.218159 | source=`proxifly`
- 21. `socks5://206.123.156.222:5413` | `socks5` | `transparent` | 200 5.651887 | source=`proxifly`
- 22. `socks5://206.123.156.177:5257` | `socks5` | `transparent` | 200 6.458280 | source=`proxifly`

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
