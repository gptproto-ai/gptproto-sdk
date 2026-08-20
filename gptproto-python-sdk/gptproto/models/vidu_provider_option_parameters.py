from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.vidu_provider_option_parameters_movement_amplitude import (
    ViduProviderOptionParametersMovementAmplitude,
)
from ..models.vidu_provider_option_parameters_style import (
    ViduProviderOptionParametersStyle,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vidu_provider_option_parameters_subjects_item import (
        ViduProviderOptionParametersSubjectsItem,
    )


T = TypeVar("T", bound="ViduProviderOptionParameters")


@_attrs_define
class ViduProviderOptionParameters:
    """
    Attributes:
        subjects (list[ViduProviderOptionParametersSubjectsItem] | Unset):
        input_image_n (int | Unset):
        template (str | Unset):
        style (ViduProviderOptionParametersStyle | Unset):
        voice_id (str | Unset):
        is_rec (bool | Unset):
        movement_amplitude (ViduProviderOptionParametersMovementAmplitude | Unset):
        bgm (bool | Unset):
        sample_count (int | Unset):
        area (str | Unset):
        beast (str | Unset):
        negative_prompt (str | Unset):
        moderation (str | Unset):
    """

    subjects: list[ViduProviderOptionParametersSubjectsItem] | Unset = UNSET
    input_image_n: int | Unset = UNSET
    template: str | Unset = UNSET
    style: ViduProviderOptionParametersStyle | Unset = UNSET
    voice_id: str | Unset = UNSET
    is_rec: bool | Unset = UNSET
    movement_amplitude: ViduProviderOptionParametersMovementAmplitude | Unset = UNSET
    bgm: bool | Unset = UNSET
    sample_count: int | Unset = UNSET
    area: str | Unset = UNSET
    beast: str | Unset = UNSET
    negative_prompt: str | Unset = UNSET
    moderation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subjects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subjects, Unset):
            subjects = []
            for subjects_item_data in self.subjects:
                subjects_item = subjects_item_data.to_dict()
                subjects.append(subjects_item)

        input_image_n = self.input_image_n

        template = self.template

        style: str | Unset = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.value

        voice_id = self.voice_id

        is_rec = self.is_rec

        movement_amplitude: str | Unset = UNSET
        if not isinstance(self.movement_amplitude, Unset):
            movement_amplitude = self.movement_amplitude.value

        bgm = self.bgm

        sample_count = self.sample_count

        area = self.area

        beast = self.beast

        negative_prompt = self.negative_prompt

        moderation = self.moderation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subjects is not UNSET:
            field_dict["subjects"] = subjects
        if input_image_n is not UNSET:
            field_dict["input_image_n"] = input_image_n
        if template is not UNSET:
            field_dict["template"] = template
        if style is not UNSET:
            field_dict["style"] = style
        if voice_id is not UNSET:
            field_dict["voice_id"] = voice_id
        if is_rec is not UNSET:
            field_dict["is_rec"] = is_rec
        if movement_amplitude is not UNSET:
            field_dict["movement_amplitude"] = movement_amplitude
        if bgm is not UNSET:
            field_dict["bgm"] = bgm
        if sample_count is not UNSET:
            field_dict["sample_count"] = sample_count
        if area is not UNSET:
            field_dict["area"] = area
        if beast is not UNSET:
            field_dict["beast"] = beast
        if negative_prompt is not UNSET:
            field_dict["negative_prompt"] = negative_prompt
        if moderation is not UNSET:
            field_dict["moderation"] = moderation

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vidu_provider_option_parameters_subjects_item import (
            ViduProviderOptionParametersSubjectsItem,
        )

        d = dict(src_dict)
        _subjects = d.pop("subjects", UNSET)
        subjects: list[ViduProviderOptionParametersSubjectsItem] | Unset = UNSET
        if _subjects is not UNSET:
            subjects = []
            for subjects_item_data in _subjects:
                subjects_item = ViduProviderOptionParametersSubjectsItem.from_dict(
                    subjects_item_data
                )

                subjects.append(subjects_item)

        input_image_n = d.pop("input_image_n", UNSET)

        template = d.pop("template", UNSET)

        _style = d.pop("style", UNSET)
        style: ViduProviderOptionParametersStyle | Unset
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = ViduProviderOptionParametersStyle(_style)

        voice_id = d.pop("voice_id", UNSET)

        is_rec = d.pop("is_rec", UNSET)

        _movement_amplitude = d.pop("movement_amplitude", UNSET)
        movement_amplitude: ViduProviderOptionParametersMovementAmplitude | Unset
        if isinstance(_movement_amplitude, Unset):
            movement_amplitude = UNSET
        else:
            movement_amplitude = ViduProviderOptionParametersMovementAmplitude(
                _movement_amplitude
            )

        bgm = d.pop("bgm", UNSET)

        sample_count = d.pop("sample_count", UNSET)

        area = d.pop("area", UNSET)

        beast = d.pop("beast", UNSET)

        negative_prompt = d.pop("negative_prompt", UNSET)

        moderation = d.pop("moderation", UNSET)

        vidu_provider_option_parameters = cls(
            subjects=subjects,
            input_image_n=input_image_n,
            template=template,
            style=style,
            voice_id=voice_id,
            is_rec=is_rec,
            movement_amplitude=movement_amplitude,
            bgm=bgm,
            sample_count=sample_count,
            area=area,
            beast=beast,
            negative_prompt=negative_prompt,
            moderation=moderation,
        )

        vidu_provider_option_parameters.additional_properties = d
        return vidu_provider_option_parameters

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
