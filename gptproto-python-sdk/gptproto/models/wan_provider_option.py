from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.wan_provider_option_parameters import WanProviderOptionParameters


T = TypeVar("T", bound="WanProviderOption")


@_attrs_define
class WanProviderOption:
    """
    Attributes:
        parameters (WanProviderOptionParameters):
    """

    parameters: WanProviderOptionParameters
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameters = self.parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parameters": parameters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wan_provider_option_parameters import WanProviderOptionParameters

        d = dict(src_dict)
        parameters = WanProviderOptionParameters.from_dict(d.pop("parameters"))

        wan_provider_option = cls(
            parameters=parameters,
        )

        wan_provider_option.additional_properties = d
        return wan_provider_option

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
