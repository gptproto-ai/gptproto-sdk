/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Unified3DRequest } from '../models/Unified3DRequest';
import type { UnifiedImageToolRequest } from '../models/UnifiedImageToolRequest';
import type { UnifiedLipSyncRequest } from '../models/UnifiedLipSyncRequest';
import type { UnifiedTaskResult } from '../models/UnifiedTaskResult';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class ExtensionsService {
    /**
     * Submit an asynchronous lip-sync task
     * @param requestBody
     * @returns UnifiedTaskResult Task accepted
     * @throws ApiError
     */
    public static createLipSync(
        requestBody: UnifiedLipSyncRequest,
    ): CancelablePromise<UnifiedTaskResult> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v3/lip-sync',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                400: `Invalid request or unsupported model`,
                401: `Missing or invalid bearer token`,
            },
        });
    }
    /**
     * Submit an asynchronous image-to-3D task
     * @param requestBody
     * @returns UnifiedTaskResult Task accepted
     * @throws ApiError
     */
    public static create3D(
        requestBody: Unified3DRequest,
    ): CancelablePromise<UnifiedTaskResult> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v3/3d',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                400: `Invalid request or unsupported model`,
                401: `Missing or invalid bearer token`,
            },
        });
    }
    /**
     * Submit an existing image/video utility task
     * @param requestBody
     * @returns UnifiedTaskResult Task accepted
     * @throws ApiError
     */
    public static createImageTool(
        requestBody: UnifiedImageToolRequest,
    ): CancelablePromise<UnifiedTaskResult> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v3/images/edit',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                400: `Invalid request or unsupported model`,
                401: `Missing or invalid bearer token`,
            },
        });
    }
}
