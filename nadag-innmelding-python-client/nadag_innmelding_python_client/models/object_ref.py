from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectRef")


@_attrs_define
class ObjectRef:
    """
    Attributes:
        lokal_id (UUID | Unset):
        navnerom (str | Unset):
        versjon_id (int | Unset):
        type_name (str | Unset):
    """

    lokal_id: UUID | Unset = UNSET
    navnerom: str | Unset = UNSET
    versjon_id: int | Unset = UNSET
    type_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lokal_id: str | Unset = UNSET
        if not isinstance(self.lokal_id, Unset):
            lokal_id = str(self.lokal_id)

        navnerom = self.navnerom

        versjon_id = self.versjon_id

        type_name = self.type_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lokal_id is not UNSET:
            field_dict["lokalId"] = lokal_id
        if navnerom is not UNSET:
            field_dict["navnerom"] = navnerom
        if versjon_id is not UNSET:
            field_dict["versjonId"] = versjon_id
        if type_name is not UNSET:
            field_dict["typeName"] = type_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _lokal_id = d.pop("lokalId", UNSET)
        lokal_id: UUID | Unset
        if isinstance(_lokal_id, Unset):
            lokal_id = UNSET
        else:
            lokal_id = UUID(_lokal_id)

        navnerom = d.pop("navnerom", UNSET)

        versjon_id = d.pop("versjonId", UNSET)

        type_name = d.pop("typeName", UNSET)

        object_ref = cls(
            lokal_id=lokal_id,
            navnerom=navnerom,
            versjon_id=versjon_id,
            type_name=type_name,
        )

        object_ref.additional_properties = d
        return object_ref

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
