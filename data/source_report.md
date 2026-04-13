# KR 免费代理自动刷新报告（2026-04-13T23:00:07+00:00）

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

- geonode: 25
- iplocate: 1
- monosans_fallback: 0
- monosans_kr_json: 14
- niek: 5
- proxifly: 17
- proxyscrape: 100
- skillter_fallback: 0
- 去重后总候选: 155

## 当前验证通过的代理

- 1. `socks5://193.122.105.251:65535` | `socks5` | `elite` | 200 1.290680 | source=`proxyscrape`
- 2. `socks5://43.133.77.87:1080` | `socks5` | `unknown` | 200 1.208131 | source=`monosans_kr_json`
- 3. `socks5://206.123.156.236:4661` | `socks5` | `unknown` | 200 3.991758 | source=`monosans_kr_json`
- 4. `socks5://206.123.156.217:4589` | `socks5` | `unknown` | 200 4.543026 | source=`monosans_kr_json`
- 5. `socks5://206.123.156.204:7102` | `socks5` | `unknown` | 200 4.636825 | source=`monosans_kr_json`
- 6. `socks5://206.123.156.178:9137` | `socks5` | `unknown` | 200 4.817002 | source=`monosans_kr_json`
- 7. `socks5://206.123.156.187:9029` | `socks5` | `unknown` | 200 4.943167 | source=`monosans_kr_json`
- 8. `socks5://206.123.156.234:6322` | `socks5` | `unknown` | 200 6.026935 | source=`monosans_kr_json`
- 9. `http://1.231.81.166:3128` | `http` | `unknown` | 200 8.286200 | source=`monosans_kr_json`
- 10. `socks5://1.225.116.115:1080` | `socks5` | `transparent` | 200 1.231756 | source=`proxifly`
- 11. `socks5://121.169.46.116:1090` | `socks5` | `transparent` | 200 1.266666 | source=`proxifly`
- 12. `socks5://206.123.156.224:8212` | `socks5` | `transparent` | 200 3.485354 | source=`proxifly`
- 13. `socks5://206.123.156.194:6748` | `socks5` | `transparent` | 200 3.890692 | source=`proxifly`
- 14. `socks5://206.123.156.223:6379` | `socks5` | `transparent` | 200 4.330356 | source=`proxifly`
- 15. `socks5://206.123.156.233:9356` | `socks5` | `transparent` | 200 5.025431 | source=`proxifly`
- 16. `socks5://206.123.156.210:6741` | `socks5` | `transparent` | 200 8.761559 | source=`proxifly`
- 17. `http://152.69.229.220:3128` | `http` | `transparent` | 200 8.043708 | source=`proxyscrape`

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
