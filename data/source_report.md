# KR 免费代理自动刷新报告（2026-05-31T18:14:57+00:00）

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

- geonode: 100
- iplocate: 2
- monosans_fallback: 0
- monosans_kr_json: 2
- niek: 22
- proxifly: 26
- proxyscrape: 46
- skillter_fallback: 0
- 去重后总候选: 176

## 当前验证通过的代理

- 1. `socks5://121.169.46.116:1090` | `socks5` | `elite` | 200 0.875823 | source=`geonode`
- 2. `socks5://211.245.23.166:1080` | `socks5` | `elite` | 200 0.915662 | source=`proxyscrape`
- 3. `socks5://152.70.237.238:3128` | `socks5` | `elite` | 200 1.321394 | source=`proxyscrape`
- 4. `socks5://158.247.206.191:1080` | `socks5` | `elite` | 200 1.392288 | source=`geonode`
- 5. `socks5://158.247.253.121:1080` | `socks5` | `elite` | 200 2.499830 | source=`proxyscrape`
- 6. `socks5://158.179.173.238:1080` | `socks5` | `elite` | 200 4.000934 | source=`geonode`
- 7. `socks5://130.162.141.185:52916` | `socks5` | `elite` | 200 4.817016 | source=`proxyscrape`
- 8. `socks4://211.245.23.166:1080` | `socks4` | `elite` | 200 0.722692 | source=`proxyscrape`
- 9. `socks4://158.247.193.221:1080` | `socks4` | `elite` | 200 1.475973 | source=`proxyscrape`
- 10. `socks4://158.247.253.121:1080` | `socks4` | `elite` | 200 6.186371 | source=`proxyscrape`
- 11. `http://210.223.44.230:3128` | `http` | `anonymous` | 200 0.681149 | source=`proxyscrape`
- 12. `http://43.128.145.26:1080` | `http` | `unknown` | 200 0.681582 | source=`monosans_kr_json`
- 13. `http://106.10.55.212:1121` | `http` | `unknown` | 200 0.862589 | source=`niek`
- 14. `http://1.231.81.166:3128` | `http` | `unknown` | 200 0.969460 | source=`monosans_kr_json`
- 15. `socks4://130.162.141.185:52916` | `socks4` | `unknown` | 200 0.675203 | source=`iplocate`
- 16. `socks5://59.11.209.162:1080` | `socks5` | `transparent` | 200 1.144844 | source=`proxifly`
- 17. `http://146.56.164.121:3128` | `http` | `transparent` | 200 0.913029 | source=`proxyscrape`
- 18. `http://121.177.104.201:3040` | `http` | `transparent` | 200 6.879827 | source=`proxifly`
- 19. `socks4://152.70.237.238:3128` | `socks4` | `transparent` | 200 2.266500 | source=`proxifly`

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
