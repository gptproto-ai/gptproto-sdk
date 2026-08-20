/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { UnifiedImageRequest } from '../models/UnifiedImageRequest';
import type { UnifiedTaskResult } from '../models/UnifiedTaskResult';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class ImageService {
    /**
     * Submit an asynchronous image generation task
     * @param requestBody
     * @returns UnifiedTaskResult Task accepted
     * @throws ApiError
     */
    public static createImage(
        requestBody: UnifiedImageRequest,
    ): CancelablePromise<UnifiedTaskResult> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v3/images',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                400: `Invalid request or unsupported model`,
                401: `Missing or invalid bearer token`,
            },
        });
    }
}
