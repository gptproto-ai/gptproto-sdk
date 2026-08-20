from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.image_reference_type import ImageReferenceType

if TYPE_CHECKING:
    from ..models.image_url import ImageUrl


T = TypeVar("T", bound="ImageReference")


@_attrs_define
class ImageReference:
    """
    Attributes:
        type_ (ImageReferenceType):
        image_url (ImageUrl):
    """

    type_: ImageReferenceType
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
        type_ = ImageReferenceType(d.pop("type"))

        image_url = ImageUrl.from_dict(d.pop("image_url"))

        image_reference = cls(
            type_=type_,
            image_url=image_url,
        )

        image_reference.additional_properties = d
        return image_reference

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
