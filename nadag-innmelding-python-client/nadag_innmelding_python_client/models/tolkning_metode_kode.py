from enum import StrEnum


class TolkningMetodeKode(StrEnum):
    BG = "BG"
    BH = "BH"
    F = "F"
    VALUE_3 = "_LE"

    def __str__(self) -> str:
        return str(self.value)
