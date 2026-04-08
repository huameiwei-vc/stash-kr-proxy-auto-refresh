# KR 免费代理自动刷新报告（2026-04-08T16:43:56+00:00）

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
- iplocate: 3
- monosans_fallback: 0
- monosans_kr_json: 4
- niek: 7
- proxifly: 29
- proxyscrape: 8
- skillter_fallback: 0
- 去重后总候选: 78

## 当前验证通过的代理

- 1. `http://112.163.160.93:3128` | `http` | `unknown` | 200 0.685952 | source=`niek`
- 2. `http://1.231.81.166:3128` | `http` | `unknown` | 200 1.065162 | source=`monosans_kr_json`
- 3. `socks5://206.123.156.208:4219` | `socks5` | `transparent` | 200 3.281467 | source=`proxifly`
- 4. `socks5://206.123.156.224:5138` | `socks5` | `transparent` | 200 3.317562 | source=`proxifly`
- 5. `socks5://206.123.156.217:6612` | `socks5` | `transparent` | 200 3.394472 | source=`proxifly`
- 6. `socks5://206.123.156.207:4675` | `socks5` | `transparent` | 200 3.880808 | source=`proxifly`
- 7. `socks5://206.123.156.216:4182` | `socks5` | `transparent` | 200 3.912767 | source=`proxifly`
- 8. `socks5://206.123.156.179:8346` | `socks5` | `transparent` | 200 4.030377 | source=`proxifly`
- 9. `socks5://206.123.156.205:5938` | `socks5` | `transparent` | 200 4.159525 | source=`proxifly`
- 10. `socks5://206.123.156.209:5516` | `socks5` | `transparent` | 200 4.162790 | source=`proxifly`
- 11. `socks5://206.123.156.212:4065` | `socks5` | `transparent` | 200 4.817517 | source=`proxifly`
- 12. `socks5://206.123.156.204:8768` | `socks5` | `transparent` | 200 4.927555 | source=`proxifly`
- 13. `socks5://206.123.156.177:4183` | `socks5` | `transparent` | 200 6.915411 | source=`proxifly`

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
