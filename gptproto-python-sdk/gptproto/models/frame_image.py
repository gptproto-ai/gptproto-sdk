from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.frame_image_frame_type import FrameImageFrameType
from ..models.frame_image_type import FrameImageType

if TYPE_CHECKING:
    from ..models.image_url import ImageUrl


T = TypeVar("T", bound="FrameImage")


@_attrs_define
class FrameImage:
    """
    Attributes:
        type_ (FrameImageType):
        frame_type (FrameImageFrameType):
        image_url (ImageUrl):
    """

    type_: FrameImageType
    frame_type: FrameImageFrameType
    image_url: ImageUrl
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        frame_type = self.frame_type.value

        image_url = self.image_url.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "frame_type": frame_type,
                "image_url": image_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.image_url import ImageUrl

        d = dict(src_dict)
        type_ = FrameImageType(d.pop("type"))

        frame_type = FrameImageFrameType(d.pop("frame_type"))

        image_url = ImageUrl.from_dict(d.pop("image_url"))

        frame_image = cls(
            type_=type_,
            frame_type=frame_type,
            image_url=image_url,
        )

        frame_image.additional_properties = d
        return frame_image

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
