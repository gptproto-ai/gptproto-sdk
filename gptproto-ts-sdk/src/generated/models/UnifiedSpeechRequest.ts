/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ProviderOptions } from './ProviderOptions';
export type UnifiedSpeechRequest = {
    model: string;
    input: string;
    /**
     * Open provider-specific voice ID.
     */
    voice: string;
    speed?: number;
    provider?: ProviderOptions;
};

