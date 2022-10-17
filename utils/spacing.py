from .exception import SnoopException


def get_ui_spacing(size: str) -> int:
    match size:
        case "sm":
            return 10
        case "lg":
            return 25
        case _:
            raise SnoopException("Invalid size for ui spacing!")
