/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ProviderOptions } from './ProviderOptions';
export type UnifiedVoiceCloneRequest = {
    model: string;
    audio: string;
    text?: string;
    custom_voice_id?: string;
    accuracy?: number;
    need_noise_reduction?: boolean;
    need_volume_normalization?: boolean;
    provider?: ProviderOptions;
};

