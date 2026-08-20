from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MinimaxProviderOptionParameters")


@_attrs_define
class MinimaxProviderOptionParameters:
    """
    Attributes:
        enable_prompt_expansion (bool | Unset):
        go_fast (bool | Unset):
        emotion (str | Unset):
        enable_base64_output (bool | Unset):
        enable_sync_mode (bool | Unset):
        english_normalization (bool | Unset):
        pitch (int | Unset):
        volume (float | Unset):
        language_boost (str | Unset):
    """

    enable_prompt_expansion: bool | Unset = UNSET
    go_fast: bool | Unset = UNSET
    emotion: str | Unset = UNSET
    enable_base64_output: bool | Unset = UNSET
    enable_sync_mode: bool | Unset = UNSET
    english_normalization: bool | Unset = UNSET
    pitch: int | Unset = UNSET
    volume: float | Unset = UNSET
    language_boost: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_prompt_expansion = self.enable_prompt_expansion

        go_fast = self.go_fast

        emotion = self.emotion

        enable_base64_output = self.enable_base64_output

        enable_sync_mode = self.enable_sync_mode

        english_normalization = self.english_normalization

        pitch = self.pitch

        volume = self.volume

        language_boost = self.language_boost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_prompt_expansion is not UNSET:
            field_dict["enable_prompt_expansion"] = enable_prompt_expansion
        if go_fast is not UNSET:
            field_dict["go_fast"] = go_fast
        if emotion is not UNSET:
            field_dict["emotion"] = emotion
        if enable_base64_output is not UNSET:
            field_dict["enable_base64_output"] = enable_base64_output
        if enable_sync_mode is not UNSET:
            field_dict["enable_sync_mode"] = enable_sync_mode
        if english_normalization is not UNSET:
            field_dict["english_normalization"] = english_normalization
        if pitch is not UNSET:
            field_dict["pitch"] = pitch
        if volume is not UNSET:
            field_dict["volume"] = volume
        if language_boost is not UNSET:
            field_dict["language_boost"] = language_boost

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable_prompt_expansion = d.pop("enable_prompt_expansion", UNSET)

        go_fast = d.pop("go_fast", UNSET)

        emotion = d.pop("emotion", UNSET)

        enable_base64_output = d.pop("enable_base64_output", UNSET)

        enable_sync_mode = d.pop("enable_sync_mode", UNSET)

        english_normalization = d.pop("english_normalization", UNSET)

        pitch = d.pop("pitch", UNSET)

        volume = d.pop("volume", UNSET)

        language_boost = d.pop("language_boost", UNSET)

        minimax_provider_option_parameters = cls(
            enable_prompt_expansion=enable_prompt_expansion,
            go_fast=go_fast,
            emotion=emotion,
            enable_base64_output=enable_base64_output,
            enable_sync_mode=enable_sync_mode,
            english_normalization=english_normalization,
            pitch=pitch,
            volume=volume,
            language_boost=language_boost,
        )

        minimax_provider_option_parameters.additional_properties = d
        return minimax_provider_option_parameters

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
