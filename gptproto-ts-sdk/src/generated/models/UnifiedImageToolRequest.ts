/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ProviderOptions } from './ProviderOptions';
/**
 * At least one of image or video is required and is enforced by the server.
 */
export type UnifiedImageToolRequest = {
    model: string;
    /**
     * Open legacy scene string.
     */
    mode?: string;
    image?: string;
    video?: string;
    creativity?: number;
    target_resolution?: string;
    size?: string;
    output_format?: UnifiedImageToolRequest.output_format;
    enable_base64_output?: boolean;
    enable_sync_mode?: boolean;
    provider?: ProviderOptions;
};
export namespace UnifiedImageToolRequest {
    export enum output_format {
        PNG = 'png',
        JPEG = 'jpeg',
        WEBP = 'webp',
        SVG = 'svg',
    }
}

