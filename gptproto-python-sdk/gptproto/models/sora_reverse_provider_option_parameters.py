from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.sora_reverse_provider_option_parameters_orientation import (
    SoraReverseProviderOptionParametersOrientation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SoraReverseProviderOptionParameters")


@_attrs_define
class SoraReverseProviderOptionParameters:
    """
    Attributes:
        timestamps (str | Unset):
        from_task (str | Unset):
        url (str | Unset):
        character_url (str | Unset):
        orientation (SoraReverseProviderOptionParametersOrientation | Unset):
        show (bool | Unset):
    """

    timestamps: str | Unset = UNSET
    from_task: str | Unset = UNSET
    url: str | Unset = UNSET
    character_url: str | Unset = UNSET
    orientation: SoraReverseProviderOptionParametersOrientation | Unset = UNSET
    show: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamps = self.timestamps

        from_task = self.from_task

        url = self.url

        character_url = self.character_url

        orientation: str | Unset = UNSET
        if not isinstance(self.orientation, Unset):
            orientation = self.orientation.value

        show = self.show

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps
        if from_task is not UNSET:
            field_dict["from_task"] = from_task
        if url is not UNSET:
            field_dict["url"] = url
        if character_url is not UNSET:
            field_dict["character_url"] = character_url
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if show is not UNSET:
            field_dict["show"] = show

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        timestamps = d.pop("timestamps", UNSET)

        from_task = d.pop("from_task", UNSET)

        url = d.pop("url", UNSET)

        character_url = d.pop("character_url", UNSET)

        _orientation = d.pop("orientation", UNSET)
        orientation: SoraReverseProviderOptionParametersOrientation | Unset
        if isinstance(_orientation, Unset):
            orientation = UNSET
        else:
            orientation = SoraReverseProviderOptionParametersOrientation(_orientation)

        show = d.pop("show", UNSET)

        sora_reverse_provider_option_parameters = cls(
            timestamps=timestamps,
            from_task=from_task,
            url=url,
            character_url=character_url,
            orientation=orientation,
            show=show,
        )

        sora_reverse_provider_option_parameters.additional_properties = d
        return sora_reverse_provider_option_parameters

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
