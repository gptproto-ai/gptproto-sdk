import { GptprotoClient } from '../src';

const baseUrl = process.env.GPTPROTO_SDK_TEST_BASE_URL;
if (!baseUrl) throw new Error('GPTPROTO_SDK_TEST_BASE_URL is required');

const client = new GptprotoClient({ baseUrl });

try {
  await client.create('video', {
    model: 'sdk-test/not-a-real-model',
    prompt: 'SDK contract probe',
  });
  throw new Error('expected the local gateway to reject the probe model');
} catch (error) {
  const apiError = error as { status?: number; body?: { error?: { code?: number } } };
  if (apiError.status !== 400 || apiError.body?.error?.code !== 400) {
    throw error;
  }
  console.log('TypeScript gateway contract: ok');
}
