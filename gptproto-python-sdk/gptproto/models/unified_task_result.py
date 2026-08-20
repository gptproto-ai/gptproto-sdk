from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.unified_task_result_status import UnifiedTaskResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unified_task_result_timings import UnifiedTaskResultTimings
    from ..models.unified_task_result_usage import UnifiedTaskResultUsage


T = TypeVar("T", bound="UnifiedTaskResult")


@_attrs_define
class UnifiedTaskResult:
    """
    Attributes:
        id (str):
        status (UnifiedTaskResultStatus):
        polling_url (str):
        generation_id (str | Unset): Returned only when the existing downstream pipeline exposes one.
        model (str | Unset):
        native_status (str | Unset): Open vendor/legacy status string; never generate as a closed enum.
        unsigned_urls (list[str] | Unset):
        error (str | Unset):
        created_at (str | Unset):
        completed_at (str | Unset): Returned only when the existing downstream pipeline exposes one.
        usage (UnifiedTaskResultUsage | Unset): Returned only when reliable existing usage data is available.
        timings (UnifiedTaskResultTimings | Unset):
    """

    id: str
    status: UnifiedTaskResultStatus
    polling_url: str
    generation_id: str | Unset = UNSET
    model: str | Unset = UNSET
    native_status: str | Unset = UNSET
    unsigned_urls: list[str] | Unset = UNSET
    error: str | Unset = UNSET
    created_at: str | Unset = UNSET
    completed_at: str | Unset = UNSET
    usage: UnifiedTaskResultUsage | Unset = UNSET
    timings: UnifiedTaskResultTimings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        polling_url = self.polling_url

        generation_id = self.generation_id

        model = self.model

        native_status = self.native_status

        unsigned_urls: list[str] | Unset = UNSET
        if not isinstance(self.unsigned_urls, Unset):
            unsigned_urls = self.unsigned_urls

        error = self.error

        created_at = self.created_at

        completed_at = self.completed_at

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        timings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timings, Unset):
            timings = self.timings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "polling_url": polling_url,
            }
        )
        if generation_id is not UNSET:
            field_dict["generation_id"] = generation_id
        if model is not UNSET:
            field_dict["model"] = model
        if native_status is not UNSET:
            field_dict["native_status"] = native_status
        if unsigned_urls is not UNSET:
            field_dict["unsigned_urls"] = unsigned_urls
        if error is not UNSET:
            field_dict["error"] = error
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if usage is not UNSET:
            field_dict["usage"] = usage
        if timings is not UNSET:
            field_dict["timings"] = timings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.unified_task_result_timings import UnifiedTaskResultTimings
        from ..models.unified_task_result_usage import UnifiedTaskResultUsage

        d = dict(src_dict)
        id = d.pop("id")

        status = UnifiedTaskResultStatus(d.pop("status"))

        polling_url = d.pop("polling_url")

        generation_id = d.pop("generation_id", UNSET)

        model = d.pop("model", UNSET)

        native_status = d.pop("native_status", UNSET)

        unsigned_urls = cast(list[str], d.pop("unsigned_urls", UNSET))

        error = d.pop("error", UNSET)

        created_at = d.pop("created_at", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        _usage = d.pop("usage", UNSET)
        usage: UnifiedTaskResultUsage | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = UnifiedTaskResultUsage.from_dict(_usage)

        _timings = d.pop("timings", UNSET)
        timings: UnifiedTaskResultTimings | Unset
        if isinstance(_timings, Unset):
            timings = UNSET
        else:
            timings = UnifiedTaskResultTimings.from_dict(_timings)

        unified_task_result = cls(
            id=id,
            status=status,
            polling_url=polling_url,
            generation_id=generation_id,
            model=model,
            native_status=native_status,
            unsigned_urls=unsigned_urls,
            error=error,
            created_at=created_at,
            completed_at=completed_at,
            usage=usage,
            timings=timings,
        )

        unified_task_result.additional_properties = d
        return unified_task_result

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
