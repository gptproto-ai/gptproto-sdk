from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_provider_option import GoogleProviderOption
    from ..models.kwaivgi_provider_option import KwaivgiProviderOption
    from ..models.minimax_provider_option import MinimaxProviderOption
    from ..models.provider_option import ProviderOption
    from ..models.seedance_provider_option import SeedanceProviderOption
    from ..models.sora_reverse_provider_option import SoraReverseProviderOption
    from ..models.vidu_provider_option import ViduProviderOption
    from ..models.wan_provider_option import WanProviderOption


T = TypeVar("T", bound="ProviderOptionsOptions")


@_attrs_define
class ProviderOptionsOptions:
    """
    Attributes:
        kwaivgi (KwaivgiProviderOption | Unset):
        kling (KwaivgiProviderOption | Unset):
        google (GoogleProviderOption | Unset):
        google_vertex (GoogleProviderOption | Unset):
        vidu (ViduProviderOption | Unset):
        bytedance (SeedanceProviderOption | Unset):
        doubao (SeedanceProviderOption | Unset):
        alibaba (WanProviderOption | Unset):
        wan (WanProviderOption | Unset):
        minimax (MinimaxProviderOption | Unset):
        openai_reverse (SoraReverseProviderOption | Unset):
    """

    kwaivgi: KwaivgiProviderOption | Unset = UNSET
    kling: KwaivgiProviderOption | Unset = UNSET
    google: GoogleProviderOption | Unset = UNSET
    google_vertex: GoogleProviderOption | Unset = UNSET
    vidu: ViduProviderOption | Unset = UNSET
    bytedance: SeedanceProviderOption | Unset = UNSET
    doubao: SeedanceProviderOption | Unset = UNSET
    alibaba: WanProviderOption | Unset = UNSET
    wan: WanProviderOption | Unset = UNSET
    minimax: MinimaxProviderOption | Unset = UNSET
    openai_reverse: SoraReverseProviderOption | Unset = UNSET
    additional_properties: dict[str, ProviderOption] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        kwaivgi: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kwaivgi, Unset):
            kwaivgi = self.kwaivgi.to_dict()

        kling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kling, Unset):
            kling = self.kling.to_dict()

        google: dict[str, Any] | Unset = UNSET
        if not isinstance(self.google, Unset):
            google = self.google.to_dict()

        google_vertex: dict[str, Any] | Unset = UNSET
        if not isinstance(self.google_vertex, Unset):
            google_vertex = self.google_vertex.to_dict()

        vidu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vidu, Unset):
            vidu = self.vidu.to_dict()

        bytedance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bytedance, Unset):
            bytedance = self.bytedance.to_dict()

        doubao: dict[str, Any] | Unset = UNSET
        if not isinstance(self.doubao, Unset):
            doubao = self.doubao.to_dict()

        alibaba: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alibaba, Unset):
            alibaba = self.alibaba.to_dict()

        wan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan, Unset):
            wan = self.wan.to_dict()

        minimax: dict[str, Any] | Unset = UNSET
        if not isinstance(self.minimax, Unset):
            minimax = self.minimax.to_dict()

        openai_reverse: dict[str, Any] | Unset = UNSET
        if not isinstance(self.openai_reverse, Unset):
            openai_reverse = self.openai_reverse.to_dict()

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})
        if kwaivgi is not UNSET:
            field_dict["kwaivgi"] = kwaivgi
        if kling is not UNSET:
            field_dict["kling"] = kling
        if google is not UNSET:
            field_dict["google"] = google
        if google_vertex is not UNSET:
            field_dict["google-vertex"] = google_vertex
        if vidu is not UNSET:
            field_dict["vidu"] = vidu
        if bytedance is not UNSET:
            field_dict["bytedance"] = bytedance
        if doubao is not UNSET:
            field_dict["doubao"] = doubao
        if alibaba is not UNSET:
            field_dict["alibaba"] = alibaba
        if wan is not UNSET:
            field_dict["wan"] = wan
        if minimax is not UNSET:
            field_dict["minimax"] = minimax
        if openai_reverse is not UNSET:
            field_dict["openai-reverse"] = openai_reverse

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.google_provider_option import GoogleProviderOption
        from ..models.kwaivgi_provider_option import KwaivgiProviderOption
        from ..models.minimax_provider_option import MinimaxProviderOption
        from ..models.provider_option import ProviderOption
        from ..models.seedance_provider_option import SeedanceProviderOption
        from ..models.sora_reverse_provider_option import SoraReverseProviderOption
        from ..models.vidu_provider_option import ViduProviderOption
        from ..models.wan_provider_option import WanProviderOption

        d = dict(src_dict)
        _kwaivgi = d.pop("kwaivgi", UNSET)
        kwaivgi: KwaivgiProviderOption | Unset
        if isinstance(_kwaivgi, Unset):
            kwaivgi = UNSET
        else:
            kwaivgi = KwaivgiProviderOption.from_dict(_kwaivgi)

        _kling = d.pop("kling", UNSET)
        kling: KwaivgiProviderOption | Unset
        if isinstance(_kling, Unset):
            kling = UNSET
        else:
            kling = KwaivgiProviderOption.from_dict(_kling)

        _google = d.pop("google", UNSET)
        google: GoogleProviderOption | Unset
        if isinstance(_google, Unset):
            google = UNSET
        else:
            google = GoogleProviderOption.from_dict(_google)

        _google_vertex = d.pop("google-vertex", UNSET)
        google_vertex: GoogleProviderOption | Unset
        if isinstance(_google_vertex, Unset):
            google_vertex = UNSET
        else:
            google_vertex = GoogleProviderOption.from_dict(_google_vertex)

        _vidu = d.pop("vidu", UNSET)
        vidu: ViduProviderOption | Unset
        if isinstance(_vidu, Unset):
            vidu = UNSET
        else:
            vidu = ViduProviderOption.from_dict(_vidu)

        _bytedance = d.pop("bytedance", UNSET)
        bytedance: SeedanceProviderOption | Unset
        if isinstance(_bytedance, Unset):
            bytedance = UNSET
        else:
            bytedance = SeedanceProviderOption.from_dict(_bytedance)

        _doubao = d.pop("doubao", UNSET)
        doubao: SeedanceProviderOption | Unset
        if isinstance(_doubao, Unset):
            doubao = UNSET
        else:
            doubao = SeedanceProviderOption.from_dict(_doubao)

        _alibaba = d.pop("alibaba", UNSET)
        alibaba: WanProviderOption | Unset
        if isinstance(_alibaba, Unset):
            alibaba = UNSET
        else:
            alibaba = WanProviderOption.from_dict(_alibaba)

        _wan = d.pop("wan", UNSET)
        wan: WanProviderOption | Unset
        if isinstance(_wan, Unset):
            wan = UNSET
        else:
            wan = WanProviderOption.from_dict(_wan)

        _minimax = d.pop("minimax", UNSET)
        minimax: MinimaxProviderOption | Unset
        if isinstance(_minimax, Unset):
            minimax = UNSET
        else:
            minimax = MinimaxProviderOption.from_dict(_minimax)

        _openai_reverse = d.pop("openai-reverse", UNSET)
        openai_reverse: SoraReverseProviderOption | Unset
        if isinstance(_openai_reverse, Unset):
            openai_reverse = UNSET
        else:
            openai_reverse = SoraReverseProviderOption.from_dict(_openai_reverse)

        provider_options_options = cls(
            kwaivgi=kwaivgi,
            kling=kling,
            google=google,
            google_vertex=google_vertex,
            vidu=vidu,
            bytedance=bytedance,
            doubao=doubao,
            alibaba=alibaba,
            wan=wan,
            minimax=minimax,
            openai_reverse=openai_reverse,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ProviderOption.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        provider_options_options.additional_properties = additional_properties
        return provider_options_options

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ProviderOption:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ProviderOption) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
