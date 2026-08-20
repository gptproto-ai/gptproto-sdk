/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type UnifiedTaskResult = {
    id: string;
    /**
     * Returned only when the existing downstream pipeline exposes one.
     */
    generation_id?: string;
    status: UnifiedTaskResult.status;
    polling_url: string;
    model?: string;
    /**
     * Open vendor/legacy status string; never generate as a closed enum.
     */
    native_status?: string;
    unsigned_urls?: Array<string>;
    error?: string;
    created_at?: string;
    /**
     * Returned only when the existing downstream pipeline exposes one.
     */
    completed_at?: string;
    /**
     * Returned only when reliable existing usage data is available.
     */
    usage?: Record<string, any>;
    timings?: Record<string, any>;
};
export namespace UnifiedTaskResult {
    export enum status {
        PENDING = 'pending',
        IN_PROGRESS = 'in_progress',
        COMPLETED = 'completed',
        FAILED = 'failed',
        CANCELLED = 'cancelled',
        EXPIRED = 'expired',
    }
}

