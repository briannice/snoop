from typing import Dict, List
from .exception import SnoopException


def format_key_value(key: str, value: str, type: str) -> str:
    result = ""
    match type:
        case "group":
            result += f"{key: <15}   →   {value}\n"
            l = len(result)
            result += "=" * (l - 1) + "\n\n"
        case "title":
            result += f"{key: <15}   →   {value}\n"
            l = len(result)
            result += "-" * (l - 1) + "\n"
        case "item":
            result += f"★ {key: <13}   →   {value}\n"
        case _:
            raise SnoopException("Invalid formatting type")
    return result


def format_key(key: str, type: str) -> str:
    result = ""
    match type:
        case "group":
            result += f"{key}\n"
            l = len(result)
            result += "-" * (l - 1) + "\n\n"
        case "title":
            result += f"{key}\n"
            l = len(result)
            result += "-" * (l - 1) + "\n"
        case "item":
            result += f"★ {key}\n"
        case _:
            raise SnoopException("Invalid formatting type")
    return result


def format_packet(contents: Dict[str, str], layer: str):
    result = ""
    layer = f"[{layer}]"
    count = 0
    for key, (value, col) in contents.items():
        if count % 2 == 0:
            result += f"{layer: <8}"
        result += f"{key: <6}"
        result += " → "
        if col == 1:
            result += f"{value: <25}"
            count += 1
        if col == 2:
            result += f"{value: <50}"
            count += 2
        if count % 2 == 0:
            result += "\n"
    if count % 2 == 1:
        result += "\n"
    return result
