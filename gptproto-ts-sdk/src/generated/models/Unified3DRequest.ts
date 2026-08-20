/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ProviderOptions } from './ProviderOptions';
export type Unified3DRequest = {
    model: string;
    /**
     * Open legacy scene string.
     */
    mode?: string;
    image: string;
    front_image_url?: string;
    back_image_url?: string;
    left_image_url?: string;
    right_image_url?: string;
    provider?: ProviderOptions;
};

