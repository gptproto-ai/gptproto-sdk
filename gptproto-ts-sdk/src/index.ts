/**
 * gptproto TypeScript SDK public entry point.
 *
 * Re-exports the generated transport (models, service, config) and the
 * hand-written run/poll layer (GptprotoClient + errors).
 */

export * from './generated/index';
export {
  GptprotoClient,
  TaskFailedError,
  TaskTimeoutError,
} from './client';
export type {
  TaskKind,
  UnifiedCreateRequest,
  RunOptions,
  ClientOptions,
} from './client';
