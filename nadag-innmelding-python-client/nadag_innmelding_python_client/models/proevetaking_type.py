from enum import StrEnum


class ProevetakingType(StrEnum):
    BLOKK = "BLOKK"
    PLASTRØR = "PLASTRØR"
    POSEPRØVE = "POSEPRØVE"
    REN_FLASKE = "REN_FLASKE"
    STERIL_FLASKE = "STERIL_FLASKE"
    SYLINDER = "SYLINDER"

    def __str__(self) -> str:
        return str(self.value)
