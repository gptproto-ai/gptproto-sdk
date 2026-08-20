import { GptprotoClient, type TaskKind } from '../src';

const baseUrl = process.env.GPTPROTO_SDK_TEST_BASE_URL;
if (!baseUrl) throw new Error('GPTPROTO_SDK_TEST_BASE_URL is required');

const client = new GptprotoClient({ baseUrl });
const requests: Array<[TaskKind, Record<string, unknown>]> = [
  ['video', { model: 'test/video', prompt: 'test' }],
  ['image', { model: 'test/image', prompt: 'test' }],
  ['speech', { model: 'test/speech', input: 'test', voice: 'test' }],
  ['voice-clone', { model: 'test/voice-clone', audio: 'https://example.invalid/audio.mp3' }],
  ['lip-sync', { model: 'test/lip-sync', video: 'https://example.invalid/video.mp4', audio: 'https://example.invalid/audio.mp3' }],
  ['3d', { model: 'test/3d', image: 'https://example.invalid/image.png' }],
  ['image-tool', { model: 'test/image-tool', image: 'https://example.invalid/image.png' }],
];

for (const [kind, body] of requests) {
  const created = await client.create(kind, body as never);
  if (created.status !== 'pending' || !created.id.startsWith('local-')) throw new Error(`bad create result for ${kind}`);
}
for (const kind of ['video', 'image'] as const) {
  const result = await client.get('local-check', kind);
  if (result.status !== 'completed') throw new Error(`bad get result for ${kind}`);
}
const completed = await client.run('video', { model: 'test/video', prompt: 'test' }, { timeout: 1_000, pollInterval: 1 });
if (completed.status !== 'completed') throw new Error('bad run result');
console.log('TypeScript local transport contract: ok');
