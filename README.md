# 韩国代理自动刷新部署包

这个目录是一个**可单独推到 GitHub 的小仓库**。

推荐架构：

- **GitHub Actions**：定时运行 `scripts/refresh_kr_stash.py`，自动刷新 `stash_kr_free.yaml`
- **Cloudflare Worker 或 Deno Deploy**：只负责提供一个稳定的订阅 URL，转发 GitHub 上最新的 YAML

## 为什么这样设计

当前验证逻辑依赖：

- `curl -x http://...`
- `curl --socks5-hostname ...`
- 实测 `http://ip-api.com/...` 判断出口是否是 KR
- 实测 `https://www.gstatic.com/generate_204` 判断 HTTPS 是否可用

所以**真正的刷新和验活**最适合放在 GitHub Actions runner 上做；
Cloudflare Worker / Deno Deploy 更适合做“稳定订阅入口”。

## 目录

- `scripts/refresh_kr_stash.py`：刷新脚本
- `.github/workflows/refresh-kr-proxy.yml`：GitHub 自动刷新
- `cloudflare-worker/`：Cloudflare Worker 转发模板
- `deno/main.ts`：Deno Deploy 转发模板
- `stash_kr_free.yaml`：最新生成的 Stash 订阅文件
- `data/`：测试结果、报告、摘要

## 部署方式 A：只用 GitHub

1. 把整个 `auto_refresh_deploy` 目录作为一个新 GitHub 仓库推上去
2. 启用 Actions
3. 等待工作流运行，或手动触发 `workflow_dispatch`
4. Stash 直接订阅：

```text
https://raw.githubusercontent.com/huameiwei-vc/stash-kr-proxy-auto-refresh/main/stash_kr_free.yaml
```

## 部署方式 B：GitHub + Cloudflare Worker

1. 先完成 GitHub 部署
2. 进入 `cloudflare-worker/`
3. 把 `wrangler.toml` 里的 `RAW_URL` 改成你的 GitHub raw 地址
4. 部署 Worker
5. Stash 使用 Worker URL 订阅

示例：

```text
https://kr-proxy-subscription.<你的子域>.workers.dev/
```

## 部署方式 C：GitHub + Deno Deploy

1. 先完成 GitHub 部署
2. 部署 `deno/main.ts`
3. 配置环境变量：

- `RAW_URL=https://raw.githubusercontent.com/huameiwei-vc/stash-kr-proxy-auto-refresh/main/stash_kr_free.yaml`

4. 用 Deno Deploy 的 URL 给 Stash 订阅

## 本地测试

```bash
python3 scripts/refresh_kr_stash.py
```

## 备注

- 免费代理波动很大，建议 GitHub Actions 至少每小时跑一次
- 如果你想更激进，可以把 cron 改成每 30 分钟甚至更短
- 但 GitHub `schedule` 触发本身可能有延迟，所以不建议把它当成秒级实时系统

## 预设仓库名

- GitHub 账号：`huameiwei-vc`
- 预设仓库名：`stash-kr-proxy-auto-refresh`
- 预设 Stash 订阅地址：

```text
https://raw.githubusercontent.com/huameiwei-vc/stash-kr-proxy-auto-refresh/main/stash_kr_free.yaml
```
