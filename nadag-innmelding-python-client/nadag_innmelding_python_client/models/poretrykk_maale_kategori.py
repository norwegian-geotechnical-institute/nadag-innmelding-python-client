from enum import StrEnum


class PoretrykkMaaleKategori(StrEnum):
    ELEKTRISK = "ELEKTRISK"
    HYDRAULISK = "HYDRAULISK"

    def __str__(self) -> str:
        return str(self.value)
