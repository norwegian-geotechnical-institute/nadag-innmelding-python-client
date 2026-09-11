from enum import StrEnum


class DeformasjonObservasjonKode(StrEnum):
    HINDRING = "HINDRING"
    IKKESPESIFISERT = "IKKESPESIFISERT"
    SKADET = "SKADET"
    USIKKERT = "USIKKERT"

    def __str__(self) -> str:
        return str(self.value)
