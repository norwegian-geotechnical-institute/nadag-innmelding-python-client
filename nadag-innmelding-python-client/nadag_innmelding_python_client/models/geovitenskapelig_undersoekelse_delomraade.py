from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifikasjon import Identifikasjon
    from ..models.polygon import Polygon


T = TypeVar("T", bound="GeovitenskapeligUndersoekelseDelomraade")


@_attrs_define
class GeovitenskapeligUndersoekelseDelomraade:
    """del av et undersøkelsesområde hvor det pågår, skal gjøres eller er gjort geovitenskapelige undersøkelser

    Merknad: Typisk brukt offshore hvor et undersøkelsesområde er delt i flere mindre lokaliteter.

    <engelsk> area where geoscientific investigations are planned, in progress or performed. Note: This feature is
    typically used offshore where an investigation is split into smaller parts</engelsk>

        Attributes:
            identifikasjon (Identifikasjon): Unik identifikasjon av et objekt, ivaretatt av den ansvarlige
                produsent/forvalter, som kan benyttes av eksterne applikasjoner som referanse til objektet.

                NOTE1 Denne eksterne objektidentifikasjonen må ikke forveksles med en tematisk objektidentifikasjon, slik som
                f.eks bygningsnummer.

                NOTE 2 Denne unike identifikatoren vil ikke endres i løpet av objektets levetid.
            område (Polygon):
            oppdateringsdato (datetime.datetime | Unset): dato for siste endring på objektetdataene

                Merknad:
                Oppdateringsdato kan være forskjellig fra Datafangsdato ved at data som er registrert kan bufres en kortere
                eller lengre periode før disse legges inn i datasystemet (databasen).

                -Definition-
                Date and time at which this version of the spatial object was inserted or changed in the spatial data set.
            beskrivelse (str | Unset): forklaring til objektet
                <engelsk>
                description of object
                </engelsk>
    """

    identifikasjon: Identifikasjon
    område: Polygon
    oppdateringsdato: datetime.datetime | Unset = UNSET
    beskrivelse: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifikasjon = self.identifikasjon.to_dict()

        område = self.område.to_dict()

        oppdateringsdato: str | Unset = UNSET
        if not isinstance(self.oppdateringsdato, Unset):
            oppdateringsdato = self.oppdateringsdato.isoformat()

        beskrivelse = self.beskrivelse

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifikasjon": identifikasjon,
                "område": område,
            }
        )
        if oppdateringsdato is not UNSET:
            field_dict["oppdateringsdato"] = oppdateringsdato
        if beskrivelse is not UNSET:
            field_dict["beskrivelse"] = beskrivelse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identifikasjon import Identifikasjon  # noqa: PLC0415
        from ..models.polygon import Polygon  # noqa: PLC0415

        d = dict(src_dict)
        identifikasjon = Identifikasjon.from_dict(d.pop("identifikasjon"))

        område = Polygon.from_dict(d.pop("område"))

        _oppdateringsdato = d.pop("oppdateringsdato", UNSET)
        oppdateringsdato: datetime.datetime | Unset
        if isinstance(_oppdateringsdato, Unset):
            oppdateringsdato = UNSET
        else:
            oppdateringsdato = datetime.datetime.fromisoformat(_oppdateringsdato)

        beskrivelse = d.pop("beskrivelse", UNSET)

        geovitenskapelig_undersoekelse_delomraade = cls(
            identifikasjon=identifikasjon,
            område=område,
            oppdateringsdato=oppdateringsdato,
            beskrivelse=beskrivelse,
        )

        geovitenskapelig_undersoekelse_delomraade.additional_properties = d
        return geovitenskapelig_undersoekelse_delomraade

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
