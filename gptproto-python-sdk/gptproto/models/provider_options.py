from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_options_options import ProviderOptionsOptions


T = TypeVar("T", bound="ProviderOptions")


@_attrs_define
class ProviderOptions:
    """Only options is public in this release; routing controls are intentionally hidden.

    Attributes:
        options (ProviderOptionsOptions | Unset):
    """

    options: ProviderOptionsOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.provider_options_options import ProviderOptionsOptions

        d = dict(src_dict)
        _options = d.pop("options", UNSET)
        options: ProviderOptionsOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = ProviderOptionsOptions.from_dict(_options)

        provider_options = cls(
            options=options,
        )

        provider_options.additional_properties = d
        return provider_options

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
