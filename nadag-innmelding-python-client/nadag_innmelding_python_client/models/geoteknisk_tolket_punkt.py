from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nadag_hoeyderef import NADAGHoeyderef
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geoteknisk_tolket_lag import GeotekniskTolketLag
    from ..models.identifikasjon import Identifikasjon
    from ..models.point import Point
    from ..models.posisjonskvalitet_nadag import PosisjonskvalitetNADAG


T = TypeVar("T", bound="GeotekniskTolketPunkt")


@_attrs_define
class GeotekniskTolketPunkt:
    """Punkt med geoteknisk tolkning i GeotekniskTolketLag

    Attributes:
        identifikasjon (Identifikasjon): Unik identifikasjon av et objekt, ivaretatt av den ansvarlige
            produsent/forvalter, som kan benyttes av eksterne applikasjoner som referanse til objektet.

            NOTE1 Denne eksterne objektidentifikasjonen må ikke forveksles med en tematisk objektidentifikasjon, slik som
            f.eks bygningsnummer.

            NOTE 2 Denne unike identifikatoren vil ikke endres i løpet av objektets levetid.
        posisjon (Point):
        h_ø_yde_referanse (NADAGHoeyderef): Brukte høydereferansesystemer i NADAG for egenskapen Høyde. EPSG-koder
            benyttes.
        tolket_av (str | Unset): Hvem som har tolket punktet
        tolket_tidspunkt (datetime.datetime | Unset): Når tolkning ble utført
        navn (str | Unset): Navn på tolket punkt
        høyde (float | Unset): Terrenghøyde overflate for punkt med tolkning(/er)[m]
        digitaliseringsmålestokk (int | Unset): kartmålestokk registreringene/ datene er hentet fra/ registrert på

            Eksempel: 1:50 000 = 50000.
        kvalitet (PosisjonskvalitetNADAG | Unset): Posisjonskvalitet slik den brukes i NADAG (Nasjonal Database for
            Grunnundersøkelser).
            (En realisering av den generelle Posisjonskvalitet)
        oppdateringsdato (datetime.datetime | Unset): dato for siste endring på objektetdataene

            Merknad:
            Oppdateringsdato kan være forskjellig fra Datafangsdato ved at data som er registrert kan bufres en kortere
            eller lengre periode før disse legges inn i datasystemet (databasen).

            -Definition-
            Date and time at which this version of the spatial object was inserted or changed in the spatial data set.
        beskrivelse (str | Unset): kort tilleggsinformasjon om punktet for tolkning/er
            <engelsk>
            a short description</engelsk>
        har_tolket_lag (list[GeotekniskTolketLag] | Unset):
    """

    identifikasjon: Identifikasjon
    posisjon: Point
    h_ø_yde_referanse: NADAGHoeyderef
    tolket_av: str | Unset = UNSET
    tolket_tidspunkt: datetime.datetime | Unset = UNSET
    navn: str | Unset = UNSET
    høyde: float | Unset = UNSET
    digitaliseringsmålestokk: int | Unset = UNSET
    kvalitet: PosisjonskvalitetNADAG | Unset = UNSET
    oppdateringsdato: datetime.datetime | Unset = UNSET
    beskrivelse: str | Unset = UNSET
    har_tolket_lag: list[GeotekniskTolketLag] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifikasjon = self.identifikasjon.to_dict()

        posisjon = self.posisjon.to_dict()

        h_ø_yde_referanse = self.h_ø_yde_referanse.value

        tolket_av = self.tolket_av

        tolket_tidspunkt: str | Unset = UNSET
        if not isinstance(self.tolket_tidspunkt, Unset):
            tolket_tidspunkt = self.tolket_tidspunkt.isoformat()

        navn = self.navn

        høyde = self.høyde

        digitaliseringsmålestokk = self.digitaliseringsmålestokk

        kvalitet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kvalitet, Unset):
            kvalitet = self.kvalitet.to_dict()

        oppdateringsdato: str | Unset = UNSET
        if not isinstance(self.oppdateringsdato, Unset):
            oppdateringsdato = self.oppdateringsdato.isoformat()

        beskrivelse = self.beskrivelse

        har_tolket_lag: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.har_tolket_lag, Unset):
            har_tolket_lag = []
            for har_tolket_lag_item_data in self.har_tolket_lag:
                har_tolket_lag_item = har_tolket_lag_item_data.to_dict()
                har_tolket_lag.append(har_tolket_lag_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifikasjon": identifikasjon,
                "posisjon": posisjon,
                "høydeReferanse": h_ø_yde_referanse,
            }
        )
        if tolket_av is not UNSET:
            field_dict["tolketAv"] = tolket_av
        if tolket_tidspunkt is not UNSET:
            field_dict["tolketTidspunkt"] = tolket_tidspunkt
        if navn is not UNSET:
            field_dict["navn"] = navn
        if høyde is not UNSET:
            field_dict["høyde"] = høyde
        if digitaliseringsmålestokk is not UNSET:
            field_dict["digitaliseringsmålestokk"] = digitaliseringsmålestokk
        if kvalitet is not UNSET:
            field_dict["kvalitet"] = kvalitet
        if oppdateringsdato is not UNSET:
            field_dict["oppdateringsdato"] = oppdateringsdato
        if beskrivelse is not UNSET:
            field_dict["beskrivelse"] = beskrivelse
        if har_tolket_lag is not UNSET:
            field_dict["harTolketLag"] = har_tolket_lag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geoteknisk_tolket_lag import GeotekniskTolketLag  # noqa: PLC0415
        from ..models.identifikasjon import Identifikasjon  # noqa: PLC0415
        from ..models.point import Point  # noqa: PLC0415
        from ..models.posisjonskvalitet_nadag import PosisjonskvalitetNADAG  # noqa: PLC0415

        d = dict(src_dict)
        identifikasjon = Identifikasjon.from_dict(d.pop("identifikasjon"))

        posisjon = Point.from_dict(d.pop("posisjon"))

        h_ø_yde_referanse = NADAGHoeyderef(d.pop("høydeReferanse"))

        tolket_av = d.pop("tolketAv", UNSET)

        _tolket_tidspunkt = d.pop("tolketTidspunkt", UNSET)
        tolket_tidspunkt: datetime.datetime | Unset
        if isinstance(_tolket_tidspunkt, Unset):
            tolket_tidspunkt = UNSET
        else:
            tolket_tidspunkt = datetime.datetime.fromisoformat(_tolket_tidspunkt)

        navn = d.pop("navn", UNSET)

        høyde = d.pop("høyde", UNSET)

        digitaliseringsmålestokk = d.pop("digitaliseringsmålestokk", UNSET)

        _kvalitet = d.pop("kvalitet", UNSET)
        kvalitet: PosisjonskvalitetNADAG | Unset
        if isinstance(_kvalitet, Unset):
            kvalitet = UNSET
        else:
            kvalitet = PosisjonskvalitetNADAG.from_dict(_kvalitet)

        _oppdateringsdato = d.pop("oppdateringsdato", UNSET)
        oppdateringsdato: datetime.datetime | Unset
        if isinstance(_oppdateringsdato, Unset):
            oppdateringsdato = UNSET
        else:
            oppdateringsdato = datetime.datetime.fromisoformat(_oppdateringsdato)

        beskrivelse = d.pop("beskrivelse", UNSET)

        _har_tolket_lag = d.pop("harTolketLag", UNSET)
        har_tolket_lag: list[GeotekniskTolketLag] | Unset = UNSET
        if _har_tolket_lag is not UNSET:
            har_tolket_lag = []
            for har_tolket_lag_item_data in _har_tolket_lag:
                har_tolket_lag_item = GeotekniskTolketLag.from_dict(har_tolket_lag_item_data)

                har_tolket_lag.append(har_tolket_lag_item)

        geoteknisk_tolket_punkt = cls(
            identifikasjon=identifikasjon,
            posisjon=posisjon,
            h_ø_yde_referanse=h_ø_yde_referanse,
            tolket_av=tolket_av,
            tolket_tidspunkt=tolket_tidspunkt,
            navn=navn,
            høyde=høyde,
            digitaliseringsmålestokk=digitaliseringsmålestokk,
            kvalitet=kvalitet,
            oppdateringsdato=oppdateringsdato,
            beskrivelse=beskrivelse,
            har_tolket_lag=har_tolket_lag,
        )

        geoteknisk_tolket_punkt.additional_properties = d
        return geoteknisk_tolket_punkt

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
