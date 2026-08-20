/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { UnifiedSpeechRequest } from '../models/UnifiedSpeechRequest';
import type { UnifiedTaskResult } from '../models/UnifiedTaskResult';
import type { UnifiedVoiceCloneRequest } from '../models/UnifiedVoiceCloneRequest';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class AudioService {
    /**
     * Submit an asynchronous text-to-speech task
     * @param requestBody
     * @returns UnifiedTaskResult Task accepted
     * @throws ApiError
     */
    public static createSpeech(
        requestBody: UnifiedSpeechRequest,
    ): CancelablePromise<UnifiedTaskResult> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v3/audio/speech',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                400: `Invalid request or unsupported model`,
                401: `Missing or invalid bearer token`,
            },
        });
    }
    /**
     * Submit an asynchronous voice-clone task
     * @param requestBody
     * @returns UnifiedTaskResult Task accepted
     * @throws ApiError
     */
    public static createVoiceClone(
        requestBody: UnifiedVoiceCloneRequest,
    ): CancelablePromise<UnifiedTaskResult> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v3/audio/voice-clone',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                400: `Invalid request or unsupported model`,
                401: `Missing or invalid bearer token`,
            },
        });
    }
}
