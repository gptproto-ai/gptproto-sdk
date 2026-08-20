/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { UnifiedTaskResult } from '../models/UnifiedTaskResult';
import type { UnifiedVideoRequest } from '../models/UnifiedVideoRequest';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class VideoService {
    /**
     * Submit an asynchronous video generation task
     * @param requestBody
     * @returns UnifiedTaskResult Task accepted
     * @throws ApiError
     */
    public static createVideo(
        requestBody: UnifiedVideoRequest,
    ): CancelablePromise<UnifiedTaskResult> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v3/videos',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                400: `Invalid request or unsupported model`,
                401: `Missing or invalid bearer token`,
            },
        });
    }
}
