/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ImageUrl } from './ImageUrl';
export type FrameImage = {
    type: FrameImage.type;
    frame_type: FrameImage.frame_type;
    image_url: ImageUrl;
};
export namespace FrameImage {
    export enum type {
        IMAGE_URL = 'image_url',
    }
    export enum frame_type {
        FIRST_FRAME = 'first_frame',
        LAST_FRAME = 'last_frame',
    }
}

