from enum import StrEnum


class VannProeveKilde(StrEnum):
    GRUNNVANN = "GRUNNVANN"
    OVERFLATEVANN = "OVERFLATEVANN"
    POREVANN = "POREVANN"
    SIGEVANN = "SIGEVANN"

    def __str__(self) -> str:
        return str(self.value)
