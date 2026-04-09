# KR 免费代理自动刷新报告（2026-04-09T11:35:24+00:00）

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

- geonode: 30
- iplocate: 0
- iplocate_error: 0
- monosans_fallback: 0
- monosans_kr_json: 98
- niek: 5
- proxifly: 183
- proxyscrape: 14
- skillter_fallback: 0
- 去重后总候选: 253

## 当前验证通过的代理

- 1. `socks5://1.234.75.15:1080` | `socks5` | `unknown` | 200 0.890755 | source=`monosans_kr_json`
- 2. `socks5://206.123.156.200:6984` | `socks5` | `unknown` | 200 3.596737 | source=`monosans_kr_json`
- 3. `socks5://206.123.156.211:7639` | `socks5` | `unknown` | 200 3.760310 | source=`monosans_kr_json`
- 4. `socks5://206.123.156.176:5885` | `socks5` | `unknown` | 200 4.408766 | source=`monosans_kr_json`
- 5. `socks5://206.123.156.216:9116` | `socks5` | `unknown` | 200 4.565258 | source=`monosans_kr_json`
- 6. `socks5://206.123.156.177:8389` | `socks5` | `unknown` | 200 5.201506 | source=`monosans_kr_json`
- 7. `socks5://206.123.156.199:10685` | `socks5` | `unknown` | 200 5.227957 | source=`monosans_kr_json`
- 8. `socks5://206.123.156.233:5366` | `socks5` | `unknown` | 200 5.924147 | source=`monosans_kr_json`
- 9. `socks5://206.123.156.217:7160` | `socks5` | `unknown` | 200 6.515010 | source=`monosans_kr_json`
- 10. `socks5://110.10.174.60:1080` | `socks5` | `unknown` | 200 8.027617 | source=`monosans_kr_json`
- 11. `socks5://206.123.156.233:7622` | `socks5` | `unknown` | 200 8.469809 | source=`monosans_kr_json`
- 12. `socks5://206.123.156.190:8337` | `socks5` | `unknown` | 200 10.251143 | source=`monosans_kr_json`
- 13. `socks5://206.123.156.189:7174` | `socks5` | `unknown` | 200 11.063264 | source=`monosans_kr_json`
- 14. `http://1.231.81.166:3128` | `http` | `unknown` | 200 1.551795 | source=`monosans_kr_json`
- 15. `socks5://121.169.46.116:1090` | `socks5` | `transparent` | 200 1.197514 | source=`proxifly`
- 16. `socks5://206.123.156.189:4376` | `socks5` | `transparent` | 200 3.266358 | source=`proxifly`
- 17. `socks5://206.123.156.224:10332` | `socks5` | `transparent` | 200 3.972337 | source=`proxifly`
- 18. `socks5://206.123.156.232:4601` | `socks5` | `transparent` | 200 5.397444 | source=`proxifly`

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
