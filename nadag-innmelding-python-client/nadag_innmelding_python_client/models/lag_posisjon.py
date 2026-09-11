from enum import StrEnum


class LagPosisjon(StrEnum):
    HØYRE = "HØYRE"
    IKKEANGITT = "IKKEANGITT"
    MIDTEN = "MIDTEN"
    VENSTRE = "VENSTRE"

    def __str__(self) -> str:
        return str(self.value)
