# KR 免费代理自动刷新报告（2026-04-13T09:07:46+00:00）

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

- geonode: 24
- iplocate: 1
- monosans_fallback: 0
- monosans_kr_json: 18
- niek: 5
- proxifly: 34
- proxyscrape: 34
- skillter_fallback: 0
- 去重后总候选: 111

## 当前验证通过的代理

- 1. `http://1.234.153.14:80` | `http` | `anonymous` | 200 0.734249 | source=`proxyscrape`
- 2. `socks5://43.133.77.87:1080` | `socks5` | `unknown` | 200 1.497813 | source=`monosans_kr_json`
- 3. `socks5://121.169.46.116:1090` | `socks5` | `transparent` | 200 1.503667 | source=`proxifly`
- 4. `http://119.195.17.15:3128` | `http` | `transparent` | 200 1.586963 | source=`proxyscrape`
- 5. `http://140.245.66.105:8081` | `http` | `transparent` | 200 5.008766 | source=`proxyscrape`
- 6. `http://61.76.102.64:3124` | `http` | `transparent` | 200 5.380651 | source=`proxyscrape`
- 7. `http://61.76.102.64:3080` | `http` | `transparent` | 200 5.839907 | source=`proxyscrape`
- 8. `http://121.176.242.215:3084` | `http` | `transparent` | 200 6.420095 | source=`proxyscrape`
- 9. `http://34.50.41.219:3128` | `http` | `transparent` | 200 10.649673 | source=`proxifly`

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
