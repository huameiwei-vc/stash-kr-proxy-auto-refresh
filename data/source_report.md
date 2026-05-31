# KR 免费代理自动刷新报告（2026-05-31T19:40:43+00:00）

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

- geonode: 106
- iplocate: 3
- monosans_fallback: 0
- monosans_kr_json: 3
- niek: 22
- proxifly: 24
- proxyscrape: 44
- skillter_fallback: 0
- 去重后总候选: 180

## 当前验证通过的代理

- 1. `socks5://121.169.46.116:1090` | `socks5` | `elite` | 200 0.819075 | source=`geonode`
- 2. `socks5://152.70.91.193:40000` | `socks5` | `elite` | 200 1.106811 | source=`geonode`
- 3. `socks5://158.180.77.24:1080` | `socks5` | `elite` | 200 1.358615 | source=`geonode`
- 4. `socks5://130.162.141.185:52916` | `socks5` | `elite` | 200 3.975850 | source=`proxyscrape`
- 5. `socks5://158.247.240.61:1080` | `socks5` | `elite` | 200 4.520447 | source=`proxyscrape`
- 6. `socks5://158.179.173.238:1080` | `socks5` | `elite` | 200 6.126116 | source=`geonode`
- 7. `socks5://152.70.237.238:3128` | `socks5` | `elite` | 200 9.592838 | source=`proxyscrape`
- 8. `socks5://222.102.194.158:1111` | `socks5` | `elite` | 200 10.714724 | source=`geonode`
- 9. `socks4://211.245.23.166:1080` | `socks4` | `elite` | 200 0.801383 | source=`proxyscrape`
- 10. `socks4://158.247.241.3:1080` | `socks4` | `elite` | 200 5.698883 | source=`proxyscrape`
- 11. `socks4://158.247.240.61:1080` | `socks4` | `elite` | 200 5.981739 | source=`proxyscrape`
- 12. `http://210.223.44.230:3128` | `http` | `anonymous` | 200 1.652095 | source=`proxyscrape`
- 13. `http://43.128.145.26:1080` | `http` | `unknown` | 200 0.637563 | source=`monosans_kr_json`
- 14. `http://125.129.15.95:3128` | `http` | `unknown` | 200 0.646887 | source=`monosans_kr_json`
- 15. `http://1.231.81.166:3128` | `http` | `unknown` | 200 0.832854 | source=`monosans_kr_json`
- 16. `socks5://211.245.23.166:1080` | `socks5` | `transparent` | 200 0.928376 | source=`proxifly`
- 17. `socks5://59.11.209.162:1080` | `socks5` | `transparent` | 200 1.032815 | source=`proxifly`
- 18. `socks5://49.167.236.96:1080` | `socks5` | `transparent` | 200 1.184185 | source=`proxifly`
- 19. `http://221.167.80.109:3076` | `http` | `transparent` | 200 2.251789 | source=`proxyscrape`
- 20. `http://112.186.12.207:3128` | `http` | `transparent` | 200 4.457648 | source=`proxyscrape`
- 21. `socks4://152.70.237.238:3128` | `socks4` | `transparent` | 200 2.093690 | source=`proxifly`

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
