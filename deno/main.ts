const RAW_URL = Deno.env.get('RAW_URL') ?? '';

Deno.serve(async (request) => {
  const url = new URL(request.url);

  if (url.pathname === '/healthz') {
    return new Response('ok', { status: 200 });
  }

  if (!RAW_URL) {
    return new Response('Missing RAW_URL env var', { status: 500 });
  }

  const upstream = await fetch(RAW_URL, {
    headers: { 'user-agent': 'kr-proxy-deno/1.0' },
  });

  if (!upstream.ok) {
    return new Response(`Upstream error: ${upstream.status}`, { status: 502 });
  }

  return new Response(await upstream.text(), {
    status: 200,
    headers: {
      'content-type': 'text/yaml; charset=utf-8',
      'cache-control': 'public, max-age=300',
    },
  });
});
