from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.point import Point


T = TypeVar("T", bound="GeotekniskUndersoekelseGrense")


@_attrs_define
class GeotekniskUndersoekelseGrense:
    """avgrensning av et område for geotekniske undersøkelser <engelsk>demarcation of an area with soil
    investigations</engelsk>

        Attributes:
            grense (Union[Unset, List['Point']]):
    """

    grense: Union[Unset, List["Point"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        grense: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.grense, Unset):
            grense = []
            for componentsschemas_line_string_item_data in self.grense:
                componentsschemas_line_string_item = componentsschemas_line_string_item_data.to_dict()
                grense.append(componentsschemas_line_string_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grense is not UNSET:
            field_dict["grense"] = grense

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.point import Point

        d = src_dict.copy()
        grense = []
        _grense = d.pop("grense", UNSET)
        for componentsschemas_line_string_item_data in _grense or []:
            componentsschemas_line_string_item = Point.from_dict(componentsschemas_line_string_item_data)

            grense.append(componentsschemas_line_string_item)

        geoteknisk_undersoekelse_grense = cls(
            grense=grense,
        )

        geoteknisk_undersoekelse_grense.additional_properties = d
        return geoteknisk_undersoekelse_grense

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
