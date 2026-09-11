from enum import StrEnum


class NADAGHoeyderef(StrEnum):
    NN2000 = "NN2000"
    NN54 = "NN54"
    UKJENT_HØYDEREFERANSE = "UKJENT_HØYDEREFERANSE"

    def __str__(self) -> str:
        return str(self.value)
