// End-to-end verification of the published gptproto TypeScript SDK against the live API.
//
// Usage:
//   export GPTPROTO_API_KEY=your_key
//   node verify_node.mjs
import { GptprotoClient } from 'gptproto';

const API_KEY = process.env.GPTPROTO_API_KEY;
const BASE_URL = process.env.GPTPROTO_BASE_URL ?? 'https://gptproto.com';

async function main() {
  if (!API_KEY) {
    console.error('Missing API key - please `export GPTPROTO_API_KEY=your_key` first');
    process.exit(1);
  }

  const client = new GptprotoClient({ apiKey: API_KEY, baseUrl: BASE_URL });

  // ---- Test 1: video task (create + get) ----
  console.log('=== Test 1: video task (create + get) ===');
  const created = await client.create('video', {
    model: 'kling/kling-v3.0-pro',
    prompt: 'a cat dancing',
    duration: 5,
  });
  console.log(`  created  taskId=${created.id}  status=${created.status}`);

  const result = await client.get(created.id, 'video');
  console.log(`  fetched  taskId=${result.id}  status=${result.status}`);

  // ---- Test 2: image task (create + get) ----
  console.log('=== Test 2: image task (create + get) ===');
  const imgCreated = await client.create('image', {
    model: 'bytedance/doubao-seedream-4-5-251128',
    prompt: 'a red apple on a table',
  });
  console.log(`  created  taskId=${imgCreated.id}  status=${imgCreated.status}`);

  const imgResult = await client.get(imgCreated.id, 'image');
  console.log(`  fetched  taskId=${imgResult.id}  status=${imgResult.status}`);

  console.log('\nAll verification checks passed');
}

main().catch((e) => {
  console.error(`Verification failed: ${e?.name ?? 'Error'}: ${e?.message ?? e}`);
  process.exit(1);
});