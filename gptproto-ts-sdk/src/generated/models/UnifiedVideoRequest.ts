/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { FrameImage } from './FrameImage';
import type { ProviderOptions } from './ProviderOptions';
import type { ReferenceAsset } from './ReferenceAsset';
import type { VideoAspectRatio } from './VideoAspectRatio';
import type { VideoResolution } from './VideoResolution';
export type UnifiedVideoRequest = {
    /**
     * Open provider/model slug; model values are not a closed enum.
     */
    model: string;
    prompt: string;
    /**
     * Open gptproto scene override; provider-specific legacy scenes are preserved.
     */
    mode?: string;
    duration?: number;
    resolution?: VideoResolution;
    aspect_ratio?: VideoAspectRatio;
    size?: string;
    frame_images?: Array<FrameImage>;
    input_references?: Array<ReferenceAsset>;
    generate_audio?: boolean | null;
    seed?: number;
    negative_prompt?: string;
    provider?: ProviderOptions;
};

