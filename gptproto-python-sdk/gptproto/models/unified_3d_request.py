from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_options import ProviderOptions


T = TypeVar("T", bound="Unified3DRequest")


@_attrs_define
class Unified3DRequest:
    """
    Attributes:
        model (str):  Example: tripo3d/tripo3d-v2.5.
        image (str):
        mode (str | Unset): Open legacy scene string. Default: 'image-to-3d'.
        front_image_url (str | Unset):
        back_image_url (str | Unset):
        left_image_url (str | Unset):
        right_image_url (str | Unset):
        provider (ProviderOptions | Unset): Only options is public in this release; routing controls are intentionally
            hidden.
    """

    model: str
    image: str
    mode: str | Unset = "image-to-3d"
    front_image_url: str | Unset = UNSET
    back_image_url: str | Unset = UNSET
    left_image_url: str | Unset = UNSET
    right_image_url: str | Unset = UNSET
    provider: ProviderOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        image = self.image

        mode = self.mode

        front_image_url = self.front_image_url

        back_image_url = self.back_image_url

        left_image_url = self.left_image_url

        right_image_url = self.right_image_url

        provider: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "image": image,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if front_image_url is not UNSET:
            field_dict["front_image_url"] = front_image_url
        if back_image_url is not UNSET:
            field_dict["back_image_url"] = back_image_url
        if left_image_url is not UNSET:
            field_dict["left_image_url"] = left_image_url
        if right_image_url is not UNSET:
            field_dict["right_image_url"] = right_image_url
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.provider_options import ProviderOptions

        d = dict(src_dict)
        model = d.pop("model")

        image = d.pop("image")

        mode = d.pop("mode", UNSET)

        front_image_url = d.pop("front_image_url", UNSET)

        back_image_url = d.pop("back_image_url", UNSET)

        left_image_url = d.pop("left_image_url", UNSET)

        right_image_url = d.pop("right_image_url", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: ProviderOptions | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = ProviderOptions.from_dict(_provider)

        unified_3d_request = cls(
            model=model,
            image=image,
            mode=mode,
            front_image_url=front_image_url,
            back_image_url=back_image_url,
            left_image_url=left_image_url,
            right_image_url=right_image_url,
            provider=provider,
        )

        unified_3d_request.additional_properties = d
        return unified_3d_request

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
