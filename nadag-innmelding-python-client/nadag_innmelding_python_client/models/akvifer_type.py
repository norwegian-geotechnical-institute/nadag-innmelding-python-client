from enum import StrEnum


class AkviferType(StrEnum):
    ARTESISK = "ARTESISK"
    IKKE_ANGITT = "IKKE_ANGITT"
    LUKKET = "LUKKET"
    UTETT = "UTETT"
    ÅPEN = "ÅPEN"

    def __str__(self) -> str:
        return str(self.value)
