#!/usr/bin/env node
import http from 'node:http';

const port = Number(process.env.GPTPROTO_SDK_TRANSPORT_PORT ?? '18082');
const expectedKey = process.env.GPTPROTO_API_KEY ?? 'local-sdk-test-key';
const createPaths = new Set([
  '/api/v3/videos',
  '/api/v3/images',
  '/api/v3/audio/speech',
  '/api/v3/audio/voice-clone',
  '/api/v3/lip-sync',
  '/api/v3/3d',
  '/api/v3/images/edit',
]);

function send(res, status, body) {
  res.writeHead(status, { 'content-type': 'application/json' });
  res.end(JSON.stringify(body));
}

const server = http.createServer(async (req, res) => {
  if (req.headers.authorization !== `Bearer ${expectedKey}`) {
    return send(res, 401, { error: { code: 401, message: 'invalid test authorization' } });
  }
  const path = new URL(req.url, 'http://127.0.0.1').pathname;
  if (req.method === 'POST' && createPaths.has(path)) {
    let raw = '';
    for await (const chunk of req) raw += chunk;
    let body;
    try { body = JSON.parse(raw); } catch { return send(res, 400, { error: { code: 400, message: 'invalid JSON' } }); }
    if (typeof body.model !== 'string' || body.model === '') {
      return send(res, 400, { error: { code: 400, message: 'model is required' } });
    }
    const id = `local-${path.split('/').filter(Boolean).join('-')}`;
    return send(res, 202, { id, status: 'pending', polling_url: `/api/v3/tasks/result/${id}` });
  }
  if (req.method === 'GET' && (/^\/api\/v3\/videos\/local-/.test(path) || /^\/api\/v3\/tasks\/result\/local-/.test(path))) {
    const id = path.slice(path.lastIndexOf('/') + 1);
    return send(res, 200, {
      id,
      status: 'completed',
      polling_url: `/api/v3/tasks/result/${id}`,
      unsigned_urls: ['https://example.invalid/result.mp4'],
    });
  }
  return send(res, 404, { error: { code: 404, message: `unexpected test route ${req.method} ${path}` } });
});

server.listen(port, '127.0.0.1', () => console.log(`SDK transport mock listening on 127.0.0.1:${port}`));
