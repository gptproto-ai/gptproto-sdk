from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.video_aspect_ratio import VideoAspectRatio
from ..models.video_resolution import VideoResolution
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frame_image import FrameImage
    from ..models.provider_options import ProviderOptions
    from ..models.reference_asset import ReferenceAsset


T = TypeVar("T", bound="UnifiedVideoRequest")


@_attrs_define
class UnifiedVideoRequest:
    """
    Attributes:
        model (str): Open provider/model slug; model values are not a closed enum. Example: kling/kling-v3.0-pro.
        prompt (str):
        mode (str | Unset): Open gptproto scene override; provider-specific legacy scenes are preserved. Default:
            'auto'. Example: image-to-video.
        duration (int | Unset):
        resolution (VideoResolution | Unset): 512, 512p, 540p and 768p are retained gptproto provider extensions.
        aspect_ratio (VideoAspectRatio | Unset): auto is a retained Vidu extension.
        size (str | Unset):  Example: 1280x720.
        frame_images (list[FrameImage] | Unset):
        input_references (list[ReferenceAsset] | Unset):
        generate_audio (bool | None | Unset):
        seed (int | Unset):
        negative_prompt (str | Unset):
        provider (ProviderOptions | Unset): Only options is public in this release; routing controls are intentionally
            hidden.
    """

    model: str
    prompt: str
    mode: str | Unset = "auto"
    duration: int | Unset = UNSET
    resolution: VideoResolution | Unset = UNSET
    aspect_ratio: VideoAspectRatio | Unset = UNSET
    size: str | Unset = UNSET
    frame_images: list[FrameImage] | Unset = UNSET
    input_references: list[ReferenceAsset] | Unset = UNSET
    generate_audio: bool | None | Unset = UNSET
    seed: int | Unset = UNSET
    negative_prompt: str | Unset = UNSET
    provider: ProviderOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        prompt = self.prompt

        mode = self.mode

        duration = self.duration

        resolution: str | Unset = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.value

        aspect_ratio: str | Unset = UNSET
        if not isinstance(self.aspect_ratio, Unset):
            aspect_ratio = self.aspect_ratio.value

        size = self.size

        frame_images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.frame_images, Unset):
            frame_images = []
            for frame_images_item_data in self.frame_images:
                frame_images_item = frame_images_item_data.to_dict()
                frame_images.append(frame_images_item)

        input_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.input_references, Unset):
            input_references = []
            for input_references_item_data in self.input_references:
                input_references_item = input_references_item_data.to_dict()
                input_references.append(input_references_item)

        generate_audio: bool | None | Unset
        if isinstance(self.generate_audio, Unset):
            generate_audio = UNSET
        else:
            generate_audio = self.generate_audio

        seed = self.seed

        negative_prompt = self.negative_prompt

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
        if mode is not UNSET:
            field_dict["mode"] = mode
        if duration is not UNSET:
            field_dict["duration"] = duration
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if aspect_ratio is not UNSET:
            field_dict["aspect_ratio"] = aspect_ratio
        if size is not UNSET:
            field_dict["size"] = size
        if frame_images is not UNSET:
            field_dict["frame_images"] = frame_images
        if input_references is not UNSET:
            field_dict["input_references"] = input_references
        if generate_audio is not UNSET:
            field_dict["generate_audio"] = generate_audio
        if seed is not UNSET:
            field_dict["seed"] = seed
        if negative_prompt is not UNSET:
            field_dict["negative_prompt"] = negative_prompt
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.frame_image import FrameImage
        from ..models.provider_options import ProviderOptions
        from ..models.reference_asset import ReferenceAsset

        d = dict(src_dict)
        model = d.pop("model")

        prompt = d.pop("prompt")

        mode = d.pop("mode", UNSET)

        duration = d.pop("duration", UNSET)

        _resolution = d.pop("resolution", UNSET)
        resolution: VideoResolution | Unset
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = VideoResolution(_resolution)

        _aspect_ratio = d.pop("aspect_ratio", UNSET)
        aspect_ratio: VideoAspectRatio | Unset
        if isinstance(_aspect_ratio, Unset):
            aspect_ratio = UNSET
        else:
            aspect_ratio = VideoAspectRatio(_aspect_ratio)

        size = d.pop("size", UNSET)

        _frame_images = d.pop("frame_images", UNSET)
        frame_images: list[FrameImage] | Unset = UNSET
        if _frame_images is not UNSET:
            frame_images = []
            for frame_images_item_data in _frame_images:
                frame_images_item = FrameImage.from_dict(frame_images_item_data)

                frame_images.append(frame_images_item)

        _input_references = d.pop("input_references", UNSET)
        input_references: list[ReferenceAsset] | Unset = UNSET
        if _input_references is not UNSET:
            input_references = []
            for input_references_item_data in _input_references:
                input_references_item = ReferenceAsset.from_dict(
                    input_references_item_data
                )

                input_references.append(input_references_item)

        def _parse_generate_audio(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        generate_audio = _parse_generate_audio(d.pop("generate_audio", UNSET))

        seed = d.pop("seed", UNSET)

        negative_prompt = d.pop("negative_prompt", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: ProviderOptions | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = ProviderOptions.from_dict(_provider)

        unified_video_request = cls(
            model=model,
            prompt=prompt,
            mode=mode,
            duration=duration,
            resolution=resolution,
            aspect_ratio=aspect_ratio,
            size=size,
            frame_images=frame_images,
            input_references=input_references,
            generate_audio=generate_audio,
            seed=seed,
            negative_prompt=negative_prompt,
            provider=provider,
        )

        unified_video_request.additional_properties = d
        return unified_video_request

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
