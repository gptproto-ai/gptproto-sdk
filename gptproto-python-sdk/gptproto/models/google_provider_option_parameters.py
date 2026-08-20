from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleProviderOptionParameters")


@_attrs_define
class GoogleProviderOptionParameters:
    """
    Attributes:
        enhance_prompt (bool | Unset):
        enable_upsample (bool | Unset):
    """

    enhance_prompt: bool | Unset = UNSET
    enable_upsample: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enhance_prompt = self.enhance_prompt

        enable_upsample = self.enable_upsample

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enhance_prompt is not UNSET:
            field_dict["enhance_prompt"] = enhance_prompt
        if enable_upsample is not UNSET:
            field_dict["enable_upsample"] = enable_upsample

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enhance_prompt = d.pop("enhance_prompt", UNSET)

        enable_upsample = d.pop("enable_upsample", UNSET)

        google_provider_option_parameters = cls(
            enhance_prompt=enhance_prompt,
            enable_upsample=enable_upsample,
        )

        google_provider_option_parameters.additional_properties = d
        return google_provider_option_parameters

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
