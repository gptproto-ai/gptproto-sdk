/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ImageAspectRatio } from './ImageAspectRatio';
import type { ImageReference } from './ImageReference';
import type { ImageResolution } from './ImageResolution';
import type { ProviderOptions } from './ProviderOptions';
export type UnifiedImageRequest = {
    model: string;
    prompt: string;
    aspect_ratio?: ImageAspectRatio;
    resolution?: ImageResolution;
    /**
     * Resolution tier or explicit pixels.
     */
    size?: string;
    'n'?: number;
    quality?: UnifiedImageRequest.quality;
    output_format?: UnifiedImageRequest.output_format;
    background?: UnifiedImageRequest.background;
    seed?: number;
    input_references?: Array<ImageReference>;
    provider?: ProviderOptions;
};
export namespace UnifiedImageRequest {
    export enum quality {
        AUTO = 'auto',
        LOW = 'low',
        MEDIUM = 'medium',
        HIGH = 'high',
    }
    export enum output_format {
        PNG = 'png',
        JPEG = 'jpeg',
        WEBP = 'webp',
        SVG = 'svg',
    }
    export enum background {
        AUTO = 'auto',
        TRANSPARENT = 'transparent',
        OPAQUE = 'opaque',
    }
}

