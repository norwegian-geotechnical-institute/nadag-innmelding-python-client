from enum import StrEnum


class KvikkleirePaavisningKode(StrEnum):
    ANTATT = "ANTATT"
    ANTATTIKKEKVIKK = "ANTATTIKKEKVIKK"
    IKKEVURDERT = "IKKEVURDERT"
    SIKKER = "SIKKER"
    USIKKER = "USIKKER"

    def __str__(self) -> str:
        return str(self.value)
