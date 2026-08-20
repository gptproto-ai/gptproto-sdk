/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ImageUrl } from './ImageUrl';
export type ReferenceAsset = {
    type: ReferenceAsset.type;
    image_url: ImageUrl;
};
export namespace ReferenceAsset {
    export enum type {
        IMAGE_URL = 'image_url',
        AUDIO_URL = 'audio_url',
        VIDEO_URL = 'video_url',
    }
}

