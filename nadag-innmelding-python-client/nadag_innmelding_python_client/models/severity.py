from enum import StrEnum


class Severity(StrEnum):
    ERROR = "ERROR"
    FATAL = "FATAL"
    OK = "OK"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
