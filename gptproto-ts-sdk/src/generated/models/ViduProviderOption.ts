/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type ViduProviderOption = {
    parameters: {
        subjects?: Array<Record<string, any>>;
        input_image_n?: number;
        template?: string;
        style?: ViduProviderOption.style;
        voice_id?: string;
        is_rec?: boolean;
        movement_amplitude?: ViduProviderOption.movement_amplitude;
        bgm?: boolean;
        sample_count?: number;
        area?: string;
        beast?: string;
        negative_prompt?: string;
        moderation?: string;
    };
};
export namespace ViduProviderOption {
    export enum style {
        GENERAL = 'general',
        ANIME = 'anime',
    }
    export enum movement_amplitude {
        AUTO = 'auto',
        SMALL = 'small',
        MEDIUM = 'medium',
        LARGE = 'large',
    }
}

