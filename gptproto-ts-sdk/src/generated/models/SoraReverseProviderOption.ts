/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type SoraReverseProviderOption = {
    parameters: {
        timestamps?: string;
        from_task?: string;
        url?: string;
        character_url?: string;
        orientation?: SoraReverseProviderOption.orientation;
        show?: boolean;
    };
};
export namespace SoraReverseProviderOption {
    export enum orientation {
        PORTRAIT = 'portrait',
        LANDSCAPE = 'landscape',
    }
}

