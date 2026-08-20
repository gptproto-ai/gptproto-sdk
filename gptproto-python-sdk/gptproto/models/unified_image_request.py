from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.image_aspect_ratio import ImageAspectRatio
from ..models.image_resolution import ImageResolution
from ..models.unified_image_request_background import UnifiedImageRequestBackground
from ..models.unified_image_request_output_format import UnifiedImageRequestOutputFormat
from ..models.unified_image_request_quality import UnifiedImageRequestQuality
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_reference import ImageReference
    from ..models.provider_options import ProviderOptions


T = TypeVar("T", bound="UnifiedImageRequest")


@_attrs_define
class UnifiedImageRequest:
    """
    Attributes:
        model (str):  Example: bytedance/doubao-seedream-4-5-251128.
        prompt (str):
        aspect_ratio (ImageAspectRatio | Unset):
        resolution (ImageResolution | Unset):
        size (str | Unset): Resolution tier or explicit pixels.
        n (int | Unset):
        quality (UnifiedImageRequestQuality | Unset):
        output_format (UnifiedImageRequestOutputFormat | Unset):
        background (UnifiedImageRequestBackground | Unset):
        seed (int | Unset):
        input_references (list[ImageReference] | Unset):
        provider (ProviderOptions | Unset): Only options is public in this release; routing controls are intentionally
            hidden.
    """

    model: str
    prompt: str
    aspect_ratio: ImageAspectRatio | Unset = UNSET
    resolution: ImageResolution | Unset = UNSET
    size: str | Unset = UNSET
    n: int | Unset = UNSET
    quality: UnifiedImageRequestQuality | Unset = UNSET
    output_format: UnifiedImageRequestOutputFormat | Unset = UNSET
    background: UnifiedImageRequestBackground | Unset = UNSET
    seed: int | Unset = UNSET
    input_references: list[ImageReference] | Unset = UNSET
    provider: ProviderOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        prompt = self.prompt

        aspect_ratio: str | Unset = UNSET
        if not isinstance(self.aspect_ratio, Unset):
            aspect_ratio = self.aspect_ratio.value

        resolution: str | Unset = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.value

        size = self.size

        n = self.n

        quality: str | Unset = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.value

        output_format: str | Unset = UNSET
        if not isinstance(self.output_format, Unset):
            output_format = self.output_format.value

        background: str | Unset = UNSET
        if not isinstance(self.background, Unset):
            background = self.background.value

        seed = self.seed

        input_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.input_references, Unset):
            input_references = []
            for input_references_item_data in self.input_references:
                input_references_item = input_references_item_data.to_dict()
                input_references.append(input_references_item)

        provider: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "prompt": prompt,
            }
        )
        if aspect_ratio is not UNSET:
            field_dict["aspect_ratio"] = aspect_ratio
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if size is not UNSET:
            field_dict["size"] = size
        if n is not UNSET:
            field_dict["n"] = n
        if quality is not UNSET:
            field_dict["quality"] = quality
        if output_format is not UNSET:
            field_dict["output_format"] = output_format
        if background is not UNSET:
            field_dict["background"] = background
        if seed is not UNSET:
            field_dict["seed"] = seed
        if input_references is not UNSET:
            field_dict["input_references"] = input_references
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.image_reference import ImageReference
        from ..models.provider_options import ProviderOptions

        d = dict(src_dict)
        model = d.pop("model")

        prompt = d.pop("prompt")

        _aspect_ratio = d.pop("aspect_ratio", UNSET)
        aspect_ratio: ImageAspectRatio | Unset
        if isinstance(_aspect_ratio, Unset):
            aspect_ratio = UNSET
        else:
            aspect_ratio = ImageAspectRatio(_aspect_ratio)

        _resolution = d.pop("resolution", UNSET)
        resolution: ImageResolution | Unset
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = ImageResolution(_resolution)

        size = d.pop("size", UNSET)

        n = d.pop("n", UNSET)

        _quality = d.pop("quality", UNSET)
        quality: UnifiedImageRequestQuality | Unset
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = UnifiedImageRequestQuality(_quality)

        _output_format = d.pop("output_format", UNSET)
        output_format: UnifiedImageRequestOutputFormat | Unset
        if isinstance(_output_format, Unset):
            output_format = UNSET
        else:
            output_format = UnifiedImageRequestOutputFormat(_output_format)

        _background = d.pop("background", UNSET)
        background: UnifiedImageRequestBackground | Unset
        if isinstance(_background, Unset):
            background = UNSET
        else:
            background = UnifiedImageRequestBackground(_background)

        seed = d.pop("seed", UNSET)

        _input_references = d.pop("input_references", UNSET)
        input_references: list[ImageReference] | Unset = UNSET
        if _input_references is not UNSET:
            input_references = []
            for input_references_item_data in _input_references:
                input_references_item = ImageReference.from_dict(
                    input_references_item_data
                )

                input_references.append(input_references_item)

        _provider = d.pop("provider", UNSET)
        provider: ProviderOptions | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = ProviderOptions.from_dict(_provider)

        unified_image_request = cls(
            model=model,
            prompt=prompt,
            aspect_ratio=aspect_ratio,
            resolution=resolution,
            size=size,
            n=n,
            quality=quality,
            output_format=output_format,
            background=background,
            seed=seed,
            input_references=input_references,
            provider=provider,
        )

        unified_image_request.additional_properties = d
        return unified_image_request

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
