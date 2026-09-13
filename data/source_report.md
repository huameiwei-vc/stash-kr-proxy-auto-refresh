# KR 免费代理自动刷新报告（2026-09-13T15:02:54+00:00）

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

- geonode: 11
- iplocate: 1
- monosans_fallback: 0
- monosans_kr_json: 6
- niek: 12
- proxifly: 18
- proxyscrape: 65
- skillter_fallback: 0
- 去重后总候选: 106

## 当前验证通过的代理

- 1. `http://121.170.165.39:25448` | `http` | `elite` | 200 0.968300 | source=`proxyscrape`
- 2. `http://121.170.165.26:21973` | `http` | `elite` | 200 0.993572 | source=`proxyscrape`
- 3. `http://121.170.165.27:21833` | `http` | `elite` | 200 1.084813 | source=`proxyscrape`
- 4. `http://203.245.16.115:18090` | `http` | `elite` | 200 1.088790 | source=`proxyscrape`
- 5. `http://121.170.165.60:27557` | `http` | `elite` | 200 1.162197 | source=`proxyscrape`
- 6. `http://210.121.160.184:22591` | `http` | `elite` | 200 1.181447 | source=`proxyscrape`
- 7. `http://210.121.160.143:12795` | `http` | `elite` | 200 1.213812 | source=`proxyscrape`
- 8. `http://121.170.165.243:28754` | `http` | `elite` | 200 1.410129 | source=`proxyscrape`
- 9. `http://121.170.165.46:13483` | `http` | `elite` | 200 1.443027 | source=`proxyscrape`
- 10. `http://121.170.165.5:13348` | `http` | `elite` | 200 2.490029 | source=`proxyscrape`
- 11. `http://210.220.138.217:16051` | `http` | `elite` | 200 2.814934 | source=`proxyscrape`
- 12. `http://121.170.165.28:17043` | `http` | `elite` | 200 3.014845 | source=`proxyscrape`
- 13. `http://121.170.165.3:24439` | `http` | `elite` | 200 3.044113 | source=`proxyscrape`
- 14. `http://210.121.160.13:26440` | `http` | `elite` | 200 3.509493 | source=`proxyscrape`
- 15. `http://210.121.160.154:14416` | `http` | `elite` | 200 3.523797 | source=`proxyscrape`
- 16. `http://210.121.160.196:23836` | `http` | `elite` | 200 5.580904 | source=`proxyscrape`
- 17. `http://210.121.160.221:21455` | `http` | `elite` | 200 5.829745 | source=`proxyscrape`
- 18. `http://210.121.160.206:18539` | `http` | `elite` | 200 7.164808 | source=`proxyscrape`
- 19. `socks5://111.119.162.248:10940` | `socks5` | `unknown` | 200 4.501549 | source=`monosans_kr_json`
- 20. `http://1.231.81.166:3128` | `http` | `unknown` | 200 0.574625 | source=`monosans_kr_json`
- 21. `http://111.119.162.248:10940` | `http` | `unknown` | 200 5.683735 | source=`monosans_kr_json`
- 22. `http://121.170.165.76:24818` | `http` | `transparent` | 200 2.805881 | source=`proxifly`

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
