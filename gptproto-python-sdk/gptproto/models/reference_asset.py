from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.reference_asset_type import ReferenceAssetType

if TYPE_CHECKING:
    from ..models.image_url import ImageUrl


T = TypeVar("T", bound="ReferenceAsset")


@_attrs_define
class ReferenceAsset:
    """
    Attributes:
        type_ (ReferenceAssetType):
        image_url (ImageUrl):
    """

    type_: ReferenceAssetType
    image_url: ImageUrl
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        image_url = self.image_url.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "image_url": image_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.image_url import ImageUrl

        d = dict(src_dict)
        type_ = ReferenceAssetType(d.pop("type"))

        image_url = ImageUrl.from_dict(d.pop("image_url"))

        reference_asset = cls(
            type_=type_,
            image_url=image_url,
        )

        reference_asset.additional_properties = d
        return reference_asset

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
