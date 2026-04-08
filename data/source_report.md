# KR 免费代理自动刷新报告（2026-04-08T11:37:08+00:00）

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
- iplocate: 9
- monosans_fallback: 0
- monosans_kr_json: 6
- niek: 7
- proxifly: 31
- proxyscrape: 10
- skillter_fallback: 0
- 去重后总候选: 83

## 当前验证通过的代理

- 1. `socks5://206.123.156.209:5516` | `socks5` | `unknown` | 200 2.860048 | source=`iplocate`
- 2. `socks5://206.123.156.224:10232` | `socks5` | `unknown` | 200 2.934475 | source=`iplocate`
- 3. `socks5://206.123.156.224:8708` | `socks5` | `unknown` | 200 3.218778 | source=`iplocate`
- 4. `socks5://206.123.156.233:5136` | `socks5` | `unknown` | 200 3.616886 | source=`monosans_kr_json`
- 5. `socks5://206.123.156.209:5058` | `socks5` | `unknown` | 200 3.846608 | source=`monosans_kr_json`
- 6. `socks5://206.123.156.222:5713` | `socks5` | `unknown` | 200 4.774958 | source=`iplocate`
- 7. `socks5://206.123.156.179:7113` | `socks5` | `unknown` | 200 5.310341 | source=`iplocate`
- 8. `socks5://206.123.156.224:4240` | `socks5` | `unknown` | 200 5.620758 | source=`iplocate`
- 9. `socks5://206.123.156.233:4221` | `socks5` | `unknown` | 200 7.711188 | source=`monosans_kr_json`
- 10. `http://1.231.81.166:3128` | `http` | `unknown` | 200 5.692934 | source=`monosans_kr_json`
- 11. `socks5://206.123.156.179:7331` | `socks5` | `transparent` | 200 2.872247 | source=`proxifly`
- 12. `socks5://206.123.156.179:4980` | `socks5` | `transparent` | 200 2.930441 | source=`proxifly`
- 13. `socks5://206.123.156.233:4539` | `socks5` | `transparent` | 200 2.954575 | source=`proxifly`
- 14. `socks5://206.123.156.189:8783` | `socks5` | `transparent` | 200 2.985206 | source=`proxifly`
- 15. `socks5://206.123.156.177:4183` | `socks5` | `transparent` | 200 3.152403 | source=`proxifly`
- 16. `socks5://206.123.156.224:4187` | `socks5` | `transparent` | 200 3.156374 | source=`proxifly`
- 17. `socks5://206.123.156.204:8768` | `socks5` | `transparent` | 200 3.165252 | source=`proxifly`
- 18. `socks5://206.123.156.205:5938` | `socks5` | `transparent` | 200 3.201224 | source=`proxifly`
- 19. `socks5://206.123.156.209:7683` | `socks5` | `transparent` | 200 3.821591 | source=`proxifly`
- 20. `socks5://206.123.156.238:4158` | `socks5` | `transparent` | 200 4.028510 | source=`proxifly`
- 21. `socks5://206.123.156.192:8633` | `socks5` | `transparent` | 200 4.301066 | source=`proxifly`
- 22. `socks5://206.123.156.188:4660` | `socks5` | `transparent` | 200 5.179127 | source=`proxifly`
- 23. `socks5://206.123.156.182:5152` | `socks5` | `transparent` | 200 5.608859 | source=`proxifly`
- 24. `socks5://206.123.156.199:5745` | `socks5` | `transparent` | 200 6.138940 | source=`proxifly`
- 25. `socks5://206.123.156.179:5440` | `socks5` | `transparent` | 200 7.568233 | source=`proxifly`

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
