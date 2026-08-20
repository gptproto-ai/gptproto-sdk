/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { UnifiedTaskResult } from '../models/UnifiedTaskResult';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class TasksService {
    /**
     * Get a video task
     * @param id
     * @returns UnifiedTaskResult Current task state
     * @throws ApiError
     */
    public static getVideoTask(
        id: string,
    ): CancelablePromise<UnifiedTaskResult> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v3/videos/{id}',
            path: {
                'id': id,
            },
            errors: {
                401: `Missing or invalid bearer token`,
            },
        });
    }
    /**
     * Get any non-video unified task
     * @param id
     * @returns UnifiedTaskResult Current task state
     * @throws ApiError
     */
    public static getTask(
        id: string,
    ): CancelablePromise<UnifiedTaskResult> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v3/tasks/result/{id}',
            path: {
                'id': id,
            },
            errors: {
                401: `Missing or invalid bearer token`,
            },
        });
    }
}
