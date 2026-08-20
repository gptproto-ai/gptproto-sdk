/** Hand-written create/poll helpers on top of the generated unified client. */
import {
  AudioService,
  ExtensionsService,
  ImageService,
  OpenAPI,
  TasksService,
  VideoService,
  type Unified3DRequest,
  type UnifiedImageRequest,
  type UnifiedImageToolRequest,
  type UnifiedLipSyncRequest,
  type UnifiedSpeechRequest,
  type UnifiedTaskResult,
  type UnifiedVideoRequest,
  type UnifiedVoiceCloneRequest,
} from './generated/index';

const SUCCESS = new Set(['completed']);
const FAILED = new Set(['failed', 'cancelled', 'expired']);

export class TaskFailedError extends Error {
  constructor(
    readonly taskId: string,
    readonly status: string,
    readonly taskError: string,
  ) {
    super(`task ${taskId} ended with ${status}: ${taskError}`);
    this.name = 'TaskFailedError';
  }
}

export class TaskTimeoutError extends Error {
  constructor(readonly taskId: string) {
    super(`task ${taskId} polling timeout`);
    this.name = 'TaskTimeoutError';
  }
}

export type TaskKind =
  | 'video'
  | 'image'
  | 'speech'
  | 'voice-clone'
  | 'lip-sync'
  | '3d'
  | 'image-tool';

export type UnifiedCreateRequest =
  | UnifiedVideoRequest
  | UnifiedImageRequest
  | UnifiedSpeechRequest
  | UnifiedVoiceCloneRequest
  | UnifiedLipSyncRequest
  | Unified3DRequest
  | UnifiedImageToolRequest;

export interface RunOptions {
  /** Total polling timeout in milliseconds. Default: 600000 (10 minutes). */
  timeout?: number;
  /** Interval between polls in milliseconds. Default: 3000. */
  pollInterval?: number;
  onStatus?: (taskId: string, status: string) => void;
}

export interface ClientOptions {
  /** API key; defaults to GPTPROTO_API_KEY. */
  apiKey?: string;
  /** API origin; defaults to https://gptproto.com. */
  baseUrl?: string;
}

export class GptprotoClient {
  constructor(opts: ClientOptions = {}) {
    const apiKey = opts.apiKey ?? process.env.GPTPROTO_API_KEY;
    if (!apiKey) {
      throw new Error('Missing API key: pass { apiKey } or set GPTPROTO_API_KEY');
    }
    OpenAPI.BASE = opts.baseUrl ?? 'https://gptproto.com';
    OpenAPI.TOKEN = apiKey;
  }

  /** Submit one task through the unified endpoint selected by kind. */
  async create(kind: TaskKind, body: UnifiedCreateRequest): Promise<UnifiedTaskResult> {
    switch (kind) {
      case 'video':
        return VideoService.createVideo(body as UnifiedVideoRequest);
      case 'image':
        return ImageService.createImage(body as UnifiedImageRequest);
      case 'speech':
        return AudioService.createSpeech(body as UnifiedSpeechRequest);
      case 'voice-clone':
        return AudioService.createVoiceClone(body as UnifiedVoiceCloneRequest);
      case 'lip-sync':
        return ExtensionsService.createLipSync(body as UnifiedLipSyncRequest);
      case '3d':
        return ExtensionsService.create3D(body as Unified3DRequest);
      case 'image-tool':
        return ExtensionsService.createImageTool(body as UnifiedImageToolRequest);
    }
  }

  /** Query once. Video uses its canonical URL; all other tasks use the shared URL. */
  get(taskId: string, kind: TaskKind = 'video'): Promise<UnifiedTaskResult> {
    return kind === 'video'
      ? TasksService.getVideoTask(taskId)
      : TasksService.getTask(taskId);
  }

  /** Submit and poll until the task reaches a terminal unified status. */
  async run(
    kind: TaskKind,
    body: UnifiedCreateRequest,
    options: RunOptions = {},
  ): Promise<UnifiedTaskResult> {
    const created = await this.create(kind, body);
    const deadline = Date.now() + (options.timeout ?? 600_000);
    const pollInterval = options.pollInterval ?? 3_000;

    while (Date.now() < deadline) {
      const result = await this.get(created.id, kind);
      const status = result.status as string;
      options.onStatus?.(created.id, status);
      if (SUCCESS.has(status)) return result;
      if (FAILED.has(status)) {
        throw new TaskFailedError(created.id, status, result.error ?? 'unknown');
      }
      await new Promise((resolve) => setTimeout(resolve, pollInterval));
    }
    throw new TaskTimeoutError(created.id);
  }
}
