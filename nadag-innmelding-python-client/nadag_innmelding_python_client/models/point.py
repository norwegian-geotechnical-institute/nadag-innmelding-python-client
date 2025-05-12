from typing import Any, Dict, List, Literal, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Point")


@_attrs_define
class Point:
    """
    Attributes:
        type (Union[Literal['Point'], Unset]):
        coordinates (Union[Unset, List[float]]):
    """

    type: Union[Literal["Point"], Unset] = UNSET
    coordinates: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        coordinates: Union[Unset, List[float]] = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = cast(Union[Literal["Point"], Unset], d.pop("type", UNSET))
        if type != "Point" and not isinstance(type, Unset):
            raise ValueError(f"type must match const 'Point', got '{type}'")

        coordinates = cast(List[float], d.pop("coordinates", UNSET))

        point = cls(
            type=type,
            coordinates=coordinates,
        )

        point.additional_properties = d
        return point

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
