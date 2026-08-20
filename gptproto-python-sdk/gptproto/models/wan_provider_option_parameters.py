from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WanProviderOptionParameters")


@_attrs_define
class WanProviderOptionParameters:
    """
    Attributes:
        enable_prompt_expansion (bool | Unset):
        watermark (bool | Unset):
        mode (str | Unset):
        shot_type (str | Unset):
        n (int | Unset):
        negative_prompt (str | Unset):
    """

    enable_prompt_expansion: bool | Unset = UNSET
    watermark: bool | Unset = UNSET
    mode: str | Unset = UNSET
    shot_type: str | Unset = UNSET
    n: int | Unset = UNSET
    negative_prompt: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_prompt_expansion = self.enable_prompt_expansion

        watermark = self.watermark

        mode = self.mode

        shot_type = self.shot_type

        n = self.n

        negative_prompt = self.negative_prompt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_prompt_expansion is not UNSET:
            field_dict["enable_prompt_expansion"] = enable_prompt_expansion
        if watermark is not UNSET:
            field_dict["watermark"] = watermark
        if mode is not UNSET:
            field_dict["mode"] = mode
        if shot_type is not UNSET:
            field_dict["shot_type"] = shot_type
        if n is not UNSET:
            field_dict["n"] = n
        if negative_prompt is not UNSET:
            field_dict["negative_prompt"] = negative_prompt

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable_prompt_expansion = d.pop("enable_prompt_expansion", UNSET)

        watermark = d.pop("watermark", UNSET)

        mode = d.pop("mode", UNSET)

        shot_type = d.pop("shot_type", UNSET)

        n = d.pop("n", UNSET)

        negative_prompt = d.pop("negative_prompt", UNSET)

        wan_provider_option_parameters = cls(
            enable_prompt_expansion=enable_prompt_expansion,
            watermark=watermark,
            mode=mode,
            shot_type=shot_type,
            n=n,
            negative_prompt=negative_prompt,
        )

        wan_provider_option_parameters.additional_properties = d
        return wan_provider_option_parameters

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
