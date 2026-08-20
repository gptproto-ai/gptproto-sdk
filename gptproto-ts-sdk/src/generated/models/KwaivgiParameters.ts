/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type KwaivgiParameters = {
    voice_id?: string;
    voice_language?: KwaivgiParameters.voice_language;
    voice_speed?: number;
    guidance_scale?: number;
    'n'?: number;
    cfg_scale?: number;
    use_custom_voice?: boolean;
    use_custom_video?: boolean;
    video_id?: string;
    video_url?: string;
    sound_effect_prompt?: string;
    bgm_prompt?: string;
    asmr_mode?: boolean;
    text?: string;
    keep_original_sound?: boolean;
    character_orientation?: KwaivgiParameters.character_orientation;
    shot_type?: KwaivgiParameters.shot_type;
    voice_list?: Array<Record<string, any>>;
    multi_prompt?: Array<Record<string, any>>;
    negative_prompt?: string;
};
export namespace KwaivgiParameters {
    export enum voice_language {
        ZH = 'zh',
        EN = 'en',
    }
    export enum character_orientation {
        IMAGE = 'image',
        VIDEO = 'video',
    }
    export enum shot_type {
        CUSTOMIZE = 'customize',
        INTELLIGENCE = 'intelligence',
    }
}

