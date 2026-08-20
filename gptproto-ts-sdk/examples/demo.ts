import { GptprotoClient, type UnifiedVideoRequest } from '../src';

const request: UnifiedVideoRequest = {
  model: 'kling/kling-v3.0-pro',
  prompt: 'a cat dancing',
  duration: 5,
};

console.log(JSON.stringify(request, null, 2));

// Live example (requires GPTPROTO_API_KEY):
// const client = new GptprotoClient();
// const result = await client.run('video', request);
// console.log(result.unsigned_urls);
void GptprotoClient;
