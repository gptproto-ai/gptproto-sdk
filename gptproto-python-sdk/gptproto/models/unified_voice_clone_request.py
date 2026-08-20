from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_options import ProviderOptions


T = TypeVar("T", bound="UnifiedVoiceCloneRequest")


@_attrs_define
class UnifiedVoiceCloneRequest:
    """
    Attributes:
        model (str):  Example: minimax/speech-2.5-hd-preview-voice-clone.
        audio (str):
        text (str | Unset):
        custom_voice_id (str | Unset):
        accuracy (float | Unset):
        need_noise_reduction (bool | Unset):
        need_volume_normalization (bool | Unset):
        provider (ProviderOptions | Unset): Only options is public in this release; routing controls are intentionally
            hidden.
    """

    model: str
    audio: str
    text: str | Unset = UNSET
    custom_voice_id: str | Unset = UNSET
    accuracy: float | Unset = UNSET
    need_noise_reduction: bool | Unset = UNSET
    need_volume_normalization: bool | Unset = UNSET
    provider: ProviderOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        audio = self.audio

        text = self.text

        custom_voice_id = self.custom_voice_id

        accuracy = self.accuracy

        need_noise_reduction = self.need_noise_reduction

        need_volume_normalization = self.need_volume_normalization

        provider: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "audio": audio,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if custom_voice_id is not UNSET:
            field_dict["custom_voice_id"] = custom_voice_id
        if accuracy is not UNSET:
            field_dict["accuracy"] = accuracy
        if need_noise_reduction is not UNSET:
            field_dict["need_noise_reduction"] = need_noise_reduction
        if need_volume_normalization is not UNSET:
            field_dict["need_volume_normalization"] = need_volume_normalization
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.provider_options import ProviderOptions

        d = dict(src_dict)
        model = d.pop("model")

        audio = d.pop("audio")

        text = d.pop("text", UNSET)

        custom_voice_id = d.pop("custom_voice_id", UNSET)

        accuracy = d.pop("accuracy", UNSET)

        need_noise_reduction = d.pop("need_noise_reduction", UNSET)

        need_volume_normalization = d.pop("need_volume_normalization", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: ProviderOptions | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = ProviderOptions.from_dict(_provider)

        unified_voice_clone_request = cls(
            model=model,
            audio=audio,
            text=text,
            custom_voice_id=custom_voice_id,
            accuracy=accuracy,
            need_noise_reduction=need_noise_reduction,
            need_volume_normalization=need_volume_normalization,
            provider=provider,
        )

        unified_voice_clone_request.additional_properties = d
        return unified_voice_clone_request

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
