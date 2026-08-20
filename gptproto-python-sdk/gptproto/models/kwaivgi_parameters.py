from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.kwaivgi_parameters_character_orientation import (
    KwaivgiParametersCharacterOrientation,
)
from ..models.kwaivgi_parameters_shot_type import KwaivgiParametersShotType
from ..models.kwaivgi_parameters_voice_language import KwaivgiParametersVoiceLanguage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kwaivgi_parameters_multi_prompt_item import (
        KwaivgiParametersMultiPromptItem,
    )
    from ..models.kwaivgi_parameters_voice_list_item import (
        KwaivgiParametersVoiceListItem,
    )


T = TypeVar("T", bound="KwaivgiParameters")


@_attrs_define
class KwaivgiParameters:
    """
    Attributes:
        voice_id (str | Unset):
        voice_language (KwaivgiParametersVoiceLanguage | Unset):
        voice_speed (float | Unset):
        guidance_scale (float | Unset):
        n (int | Unset):
        cfg_scale (float | Unset):
        use_custom_voice (bool | Unset):
        use_custom_video (bool | Unset):
        video_id (str | Unset):
        video_url (str | Unset):
        sound_effect_prompt (str | Unset):
        bgm_prompt (str | Unset):
        asmr_mode (bool | Unset):
        text (str | Unset):
        keep_original_sound (bool | Unset):
        character_orientation (KwaivgiParametersCharacterOrientation | Unset):
        shot_type (KwaivgiParametersShotType | Unset):
        voice_list (list[KwaivgiParametersVoiceListItem] | Unset):
        multi_prompt (list[KwaivgiParametersMultiPromptItem] | Unset):
        negative_prompt (str | Unset):
    """

    voice_id: str | Unset = UNSET
    voice_language: KwaivgiParametersVoiceLanguage | Unset = UNSET
    voice_speed: float | Unset = UNSET
    guidance_scale: float | Unset = UNSET
    n: int | Unset = UNSET
    cfg_scale: float | Unset = UNSET
    use_custom_voice: bool | Unset = UNSET
    use_custom_video: bool | Unset = UNSET
    video_id: str | Unset = UNSET
    video_url: str | Unset = UNSET
    sound_effect_prompt: str | Unset = UNSET
    bgm_prompt: str | Unset = UNSET
    asmr_mode: bool | Unset = UNSET
    text: str | Unset = UNSET
    keep_original_sound: bool | Unset = UNSET
    character_orientation: KwaivgiParametersCharacterOrientation | Unset = UNSET
    shot_type: KwaivgiParametersShotType | Unset = UNSET
    voice_list: list[KwaivgiParametersVoiceListItem] | Unset = UNSET
    multi_prompt: list[KwaivgiParametersMultiPromptItem] | Unset = UNSET
    negative_prompt: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        voice_id = self.voice_id

        voice_language: str | Unset = UNSET
        if not isinstance(self.voice_language, Unset):
            voice_language = self.voice_language.value

        voice_speed = self.voice_speed

        guidance_scale = self.guidance_scale

        n = self.n

        cfg_scale = self.cfg_scale

        use_custom_voice = self.use_custom_voice

        use_custom_video = self.use_custom_video

        video_id = self.video_id

        video_url = self.video_url

        sound_effect_prompt = self.sound_effect_prompt

        bgm_prompt = self.bgm_prompt

        asmr_mode = self.asmr_mode

        text = self.text

        keep_original_sound = self.keep_original_sound

        character_orientation: str | Unset = UNSET
        if not isinstance(self.character_orientation, Unset):
            character_orientation = self.character_orientation.value

        shot_type: str | Unset = UNSET
        if not isinstance(self.shot_type, Unset):
            shot_type = self.shot_type.value

        voice_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.voice_list, Unset):
            voice_list = []
            for voice_list_item_data in self.voice_list:
                voice_list_item = voice_list_item_data.to_dict()
                voice_list.append(voice_list_item)

        multi_prompt: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multi_prompt, Unset):
            multi_prompt = []
            for multi_prompt_item_data in self.multi_prompt:
                multi_prompt_item = multi_prompt_item_data.to_dict()
                multi_prompt.append(multi_prompt_item)

        negative_prompt = self.negative_prompt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if voice_id is not UNSET:
            field_dict["voice_id"] = voice_id
        if voice_language is not UNSET:
            field_dict["voice_language"] = voice_language
        if voice_speed is not UNSET:
            field_dict["voice_speed"] = voice_speed
        if guidance_scale is not UNSET:
            field_dict["guidance_scale"] = guidance_scale
        if n is not UNSET:
            field_dict["n"] = n
        if cfg_scale is not UNSET:
            field_dict["cfg_scale"] = cfg_scale
        if use_custom_voice is not UNSET:
            field_dict["use_custom_voice"] = use_custom_voice
        if use_custom_video is not UNSET:
            field_dict["use_custom_video"] = use_custom_video
        if video_id is not UNSET:
            field_dict["video_id"] = video_id
        if video_url is not UNSET:
            field_dict["video_url"] = video_url
        if sound_effect_prompt is not UNSET:
            field_dict["sound_effect_prompt"] = sound_effect_prompt
        if bgm_prompt is not UNSET:
            field_dict["bgm_prompt"] = bgm_prompt
        if asmr_mode is not UNSET:
            field_dict["asmr_mode"] = asmr_mode
        if text is not UNSET:
            field_dict["text"] = text
        if keep_original_sound is not UNSET:
            field_dict["keep_original_sound"] = keep_original_sound
        if character_orientation is not UNSET:
            field_dict["character_orientation"] = character_orientation
        if shot_type is not UNSET:
            field_dict["shot_type"] = shot_type
        if voice_list is not UNSET:
            field_dict["voice_list"] = voice_list
        if multi_prompt is not UNSET:
            field_dict["multi_prompt"] = multi_prompt
        if negative_prompt is not UNSET:
            field_dict["negative_prompt"] = negative_prompt

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.kwaivgi_parameters_multi_prompt_item import (
            KwaivgiParametersMultiPromptItem,
        )
        from ..models.kwaivgi_parameters_voice_list_item import (
            KwaivgiParametersVoiceListItem,
        )

        d = dict(src_dict)
        voice_id = d.pop("voice_id", UNSET)

        _voice_language = d.pop("voice_language", UNSET)
        voice_language: KwaivgiParametersVoiceLanguage | Unset
        if isinstance(_voice_language, Unset):
            voice_language = UNSET
        else:
            voice_language = KwaivgiParametersVoiceLanguage(_voice_language)

        voice_speed = d.pop("voice_speed", UNSET)

        guidance_scale = d.pop("guidance_scale", UNSET)

        n = d.pop("n", UNSET)

        cfg_scale = d.pop("cfg_scale", UNSET)

        use_custom_voice = d.pop("use_custom_voice", UNSET)

        use_custom_video = d.pop("use_custom_video", UNSET)

        video_id = d.pop("video_id", UNSET)

        video_url = d.pop("video_url", UNSET)

        sound_effect_prompt = d.pop("sound_effect_prompt", UNSET)

        bgm_prompt = d.pop("bgm_prompt", UNSET)

        asmr_mode = d.pop("asmr_mode", UNSET)

        text = d.pop("text", UNSET)

        keep_original_sound = d.pop("keep_original_sound", UNSET)

        _character_orientation = d.pop("character_orientation", UNSET)
        character_orientation: KwaivgiParametersCharacterOrientation | Unset
        if isinstance(_character_orientation, Unset):
            character_orientation = UNSET
        else:
            character_orientation = KwaivgiParametersCharacterOrientation(
                _character_orientation
            )

        _shot_type = d.pop("shot_type", UNSET)
        shot_type: KwaivgiParametersShotType | Unset
        if isinstance(_shot_type, Unset):
            shot_type = UNSET
        else:
            shot_type = KwaivgiParametersShotType(_shot_type)

        _voice_list = d.pop("voice_list", UNSET)
        voice_list: list[KwaivgiParametersVoiceListItem] | Unset = UNSET
        if _voice_list is not UNSET:
            voice_list = []
            for voice_list_item_data in _voice_list:
                voice_list_item = KwaivgiParametersVoiceListItem.from_dict(
                    voice_list_item_data
                )

                voice_list.append(voice_list_item)

        _multi_prompt = d.pop("multi_prompt", UNSET)
        multi_prompt: list[KwaivgiParametersMultiPromptItem] | Unset = UNSET
        if _multi_prompt is not UNSET:
            multi_prompt = []
            for multi_prompt_item_data in _multi_prompt:
                multi_prompt_item = KwaivgiParametersMultiPromptItem.from_dict(
                    multi_prompt_item_data
                )

                multi_prompt.append(multi_prompt_item)

        negative_prompt = d.pop("negative_prompt", UNSET)

        kwaivgi_parameters = cls(
            voice_id=voice_id,
            voice_language=voice_language,
            voice_speed=voice_speed,
            guidance_scale=guidance_scale,
            n=n,
            cfg_scale=cfg_scale,
            use_custom_voice=use_custom_voice,
            use_custom_video=use_custom_video,
            video_id=video_id,
            video_url=video_url,
            sound_effect_prompt=sound_effect_prompt,
            bgm_prompt=bgm_prompt,
            asmr_mode=asmr_mode,
            text=text,
            keep_original_sound=keep_original_sound,
            character_orientation=character_orientation,
            shot_type=shot_type,
            voice_list=voice_list,
            multi_prompt=multi_prompt,
            negative_prompt=negative_prompt,
        )

        kwaivgi_parameters.additional_properties = d
        return kwaivgi_parameters

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
