from enum import StrEnum


class KvalitetBorlengdeTilBerg(StrEnum):
    ANTATT = "ANTATT"
    PÅVIST = "PÅVIST"

    def __str__(self) -> str:
        return str(self.value)
