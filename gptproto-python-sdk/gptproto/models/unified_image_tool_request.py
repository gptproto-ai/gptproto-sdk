from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.unified_image_tool_request_output_format import (
    UnifiedImageToolRequestOutputFormat,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_options import ProviderOptions


T = TypeVar("T", bound="UnifiedImageToolRequest")


@_attrs_define
class UnifiedImageToolRequest:
    """At least one of image or video is required and is enforced by the server.

    Attributes:
        model (str):  Example: gptproto/image-upscaler.
        mode (str | Unset): Open legacy scene string. Default: 'upscale'.
        image (str | Unset):
        video (str | Unset):
        creativity (int | Unset):
        target_resolution (str | Unset):
        size (str | Unset):
        output_format (UnifiedImageToolRequestOutputFormat | Unset):
        enable_base64_output (bool | Unset):
        enable_sync_mode (bool | Unset):
        provider (ProviderOptions | Unset): Only options is public in this release; routing controls are intentionally
            hidden.
    """

    model: str
    mode: str | Unset = "upscale"
    image: str | Unset = UNSET
    video: str | Unset = UNSET
    creativity: int | Unset = UNSET
    target_resolution: str | Unset = UNSET
    size: str | Unset = UNSET
    output_format: UnifiedImageToolRequestOutputFormat | Unset = UNSET
    enable_base64_output: bool | Unset = UNSET
    enable_sync_mode: bool | Unset = UNSET
    provider: ProviderOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        mode = self.mode

        image = self.image

        video = self.video

        creativity = self.creativity

        target_resolution = self.target_resolution

        size = self.size

        output_format: str | Unset = UNSET
        if not isinstance(self.output_format, Unset):
            output_format = self.output_format.value

        enable_base64_output = self.enable_base64_output

        enable_sync_mode = self.enable_sync_mode

        provider: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if image is not UNSET:
            field_dict["image"] = image
        if video is not UNSET:
            field_dict["video"] = video
        if creativity is not UNSET:
            field_dict["creativity"] = creativity
        if target_resolution is not UNSET:
            field_dict["target_resolution"] = target_resolution
        if size is not UNSET:
            field_dict["size"] = size
        if output_format is not UNSET:
            field_dict["output_format"] = output_format
        if enable_base64_output is not UNSET:
            field_dict["enable_base64_output"] = enable_base64_output
        if enable_sync_mode is not UNSET:
            field_dict["enable_sync_mode"] = enable_sync_mode
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.provider_options import ProviderOptions

        d = dict(src_dict)
        model = d.pop("model")

        mode = d.pop("mode", UNSET)

        image = d.pop("image", UNSET)

        video = d.pop("video", UNSET)

        creativity = d.pop("creativity", UNSET)

        target_resolution = d.pop("target_resolution", UNSET)

        size = d.pop("size", UNSET)

        _output_format = d.pop("output_format", UNSET)
        output_format: UnifiedImageToolRequestOutputFormat | Unset
        if isinstance(_output_format, Unset):
            output_format = UNSET
        else:
            output_format = UnifiedImageToolRequestOutputFormat(_output_format)

        enable_base64_output = d.pop("enable_base64_output", UNSET)

        enable_sync_mode = d.pop("enable_sync_mode", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: ProviderOptions | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = ProviderOptions.from_dict(_provider)

        unified_image_tool_request = cls(
            model=model,
            mode=mode,
            image=image,
            video=video,
            creativity=creativity,
            target_resolution=target_resolution,
            size=size,
            output_format=output_format,
            enable_base64_output=enable_base64_output,
            enable_sync_mode=enable_sync_mode,
            provider=provider,
        )

        unified_image_tool_request.additional_properties = d
        return unified_image_tool_request

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
