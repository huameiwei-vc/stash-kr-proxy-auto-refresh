export interface Env {
  RAW_URL: string;
}

const YAML_HEADERS = {
  'content-type': 'text/yaml; charset=utf-8',
  'cache-control': 'public, max-age=300',
};

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);

    if (url.pathname === '/healthz') {
      return new Response('ok', { status: 200 });
    }

    if (!env.RAW_URL) {
      return new Response('Missing RAW_URL env var', { status: 500 });
    }

    const upstream = await fetch(env.RAW_URL, {
      headers: { 'user-agent': 'kr-proxy-worker/1.0' },
      cf: { cacheTtl: 300, cacheEverything: true },
    });

    if (!upstream.ok) {
      return new Response(`Upstream error: ${upstream.status}`, { status: 502 });
    }

    const text = await upstream.text();
    return new Response(text, { status: 200, headers: YAML_HEADERS });
  },
};
