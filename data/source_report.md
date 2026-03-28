# KR 免费代理自动刷新报告（2026-03-28T17:53:38+08:00）

> 目标：自动抓取并验证当前可用于 Stash 的韩国代理，仅在当前目录生成结果。

## 采用的自动化来源

1. **ProxyScrape 官方 API**  
   - <https://api.proxyscrape.com/v4/free-proxy-list/get?request=get_proxies&country=KR&proxy_format=protocolipport&format=json&skip=0&limit=100>
2. **Proxifly 韩国国家列表**  
   - <https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/countries/KR/data.json>
3. **iplocate 韩国国家列表**  
   - <https://raw.githubusercontent.com/iplocate/free-proxy-list/main/countries/KR/proxies.txt>
4. **monosans 通用列表（仅在前述来源不足时作为网络搜索后的兜底）**  
   - <https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt>  
   - <https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt>

## 原始候选数量

- iplocate: 1
- monosans_fallback: 0
- proxifly: 8
- proxyscrape: 19
- 去重后总候选: 27

## 当前验证通过的代理

- 1. `http://121.126.185.63:25152` | `http` | `elite` | 204 3.584051 | source=`proxyscrape`
- 2. `http://210.223.44.230:3128` | `http` | `anonymous` | 204 0.493931 | source=`proxyscrape`
- 3. `socks5://121.169.46.116:1090` | `socks5` | `transparent` | 204 0.431391 | source=`proxifly`
- 4. `http://1.231.81.166:3128` | `http` | `transparent` | 204 0.311856 | source=`proxyscrape`

## 输出文件

- Stash 配置：`/Users/songchao/Documents/git/2api/注册机/注册机学习/家宽/auto_refresh_deploy/stash_kr_free.yaml`
- 测试明细：`/Users/songchao/Documents/git/2api/注册机/注册机学习/家宽/auto_refresh_deploy/data/tested_kr_proxies.json`
- 运行摘要：`/Users/songchao/Documents/git/2api/注册机/注册机学习/家宽/auto_refresh_deploy/data/run_summary.json`
- 本脚本：`/Users/songchao/Documents/git/2api/注册机/注册机学习/家宽/auto_refresh_deploy/data/refresh_kr_stash.py`

## 说明

- 只保留同时满足 **KR 出口** 和 **HTTPS 可连** 的代理。
- `节点选择` 默认先给你 `KR-安全自动测速`，再给 `KR-全量自动测速`。
- 免费代理波动很大，建议用前再执行一次刷新脚本。
