from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeedanceProviderOptionParameters")


@_attrs_define
class SeedanceProviderOptionParameters:
    """
    Attributes:
        camera_fixed (bool | Unset):
        media_files (list[str] | Unset):
        is_upload_media (bool | Unset):
    """

    camera_fixed: bool | Unset = UNSET
    media_files: list[str] | Unset = UNSET
    is_upload_media: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        camera_fixed = self.camera_fixed

        media_files: list[str] | Unset = UNSET
        if not isinstance(self.media_files, Unset):
            media_files = self.media_files

        is_upload_media = self.is_upload_media

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if camera_fixed is not UNSET:
            field_dict["camera_fixed"] = camera_fixed
        if media_files is not UNSET:
            field_dict["media_files"] = media_files
        if is_upload_media is not UNSET:
            field_dict["is_upload_media"] = is_upload_media

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        camera_fixed = d.pop("camera_fixed", UNSET)

        media_files = cast(list[str], d.pop("media_files", UNSET))

        is_upload_media = d.pop("is_upload_media", UNSET)

        seedance_provider_option_parameters = cls(
            camera_fixed=camera_fixed,
            media_files=media_files,
            is_upload_media=is_upload_media,
        )

        seedance_provider_option_parameters.additional_properties = d
        return seedance_provider_option_parameters

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
