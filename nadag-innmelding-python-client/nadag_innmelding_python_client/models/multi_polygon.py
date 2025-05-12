from typing import Any, Dict, List, Literal, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiPolygon")


@_attrs_define
class MultiPolygon:
    """
    Attributes:
        type (Union[Literal['MultiPolygon'], Unset]):
        coordinates (Union[Unset, List[List[List[List[float]]]]]):
    """

    type: Union[Literal["MultiPolygon"], Unset] = UNSET
    coordinates: Union[Unset, List[List[List[List[float]]]]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        coordinates: Union[Unset, List[List[List[List[float]]]]] = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = []
            for coordinates_item_data in self.coordinates:
                coordinates_item = []
                for componentsschemas_coordinates_lists_item_data in coordinates_item_data:
                    componentsschemas_coordinates_lists_item = []
                    for componentsschemas_coordinates_list_item_data in componentsschemas_coordinates_lists_item_data:
                        componentsschemas_coordinates_list_item = componentsschemas_coordinates_list_item_data

                        componentsschemas_coordinates_lists_item.append(componentsschemas_coordinates_list_item)

                    coordinates_item.append(componentsschemas_coordinates_lists_item)

                coordinates.append(coordinates_item)

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
        type = cast(Union[Literal["MultiPolygon"], Unset], d.pop("type", UNSET))
        if type != "MultiPolygon" and not isinstance(type, Unset):
            raise ValueError(f"type must match const 'MultiPolygon', got '{type}'")

        coordinates = []
        _coordinates = d.pop("coordinates", UNSET)
        for coordinates_item_data in _coordinates or []:
            coordinates_item = []
            _coordinates_item = coordinates_item_data
            for componentsschemas_coordinates_lists_item_data in _coordinates_item:
                componentsschemas_coordinates_lists_item = []
                _componentsschemas_coordinates_lists_item = componentsschemas_coordinates_lists_item_data
                for componentsschemas_coordinates_list_item_data in _componentsschemas_coordinates_lists_item:
                    componentsschemas_coordinates_list_item = cast(
                        List[float], componentsschemas_coordinates_list_item_data
                    )

                    componentsschemas_coordinates_lists_item.append(componentsschemas_coordinates_list_item)

                coordinates_item.append(componentsschemas_coordinates_lists_item)

            coordinates.append(coordinates_item)

        multi_polygon = cls(
            type=type,
            coordinates=coordinates,
        )

        multi_polygon.additional_properties = d
        return multi_polygon

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
