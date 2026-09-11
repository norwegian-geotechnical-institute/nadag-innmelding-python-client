from enum import StrEnum


class FeltUndersTypeKode(StrEnum):
    FELTUNDERSMETODE = "FELTUNDERSMETODE"
    TOLKET = "TOLKET"
    TOLKETBERGHØYDE = "TOLKETBERGHØYDE"

    def __str__(self) -> str:
        return str(self.value)
