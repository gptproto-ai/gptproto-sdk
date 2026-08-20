from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_options import ProviderOptions


T = TypeVar("T", bound="UnifiedSpeechRequest")


@_attrs_define
class UnifiedSpeechRequest:
    """
    Attributes:
        model (str):  Example: minimax/speech-02-hd.
        input_ (str):
        voice (str): Open provider-specific voice ID.
        speed (float | Unset):
        provider (ProviderOptions | Unset): Only options is public in this release; routing controls are intentionally
            hidden.
    """

    model: str
    input_: str
    voice: str
    speed: float | Unset = UNSET
    provider: ProviderOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        input_ = self.input_

        voice = self.voice

        speed = self.speed

        provider: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "input": input_,
                "voice": voice,
            }
        )
        if speed is not UNSET:
            field_dict["speed"] = speed
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.provider_options import ProviderOptions

        d = dict(src_dict)
        model = d.pop("model")

        input_ = d.pop("input")

        voice = d.pop("voice")

        speed = d.pop("speed", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: ProviderOptions | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = ProviderOptions.from_dict(_provider)

        unified_speech_request = cls(
            model=model,
            input_=input_,
            voice=voice,
            speed=speed,
            provider=provider,
        )

        unified_speech_request.additional_properties = d
        return unified_speech_request

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
