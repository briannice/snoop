from datetime import timedelta
from typing import Dict, List
from .exception import SnoopException


def format_seconds_to_time(sec: int):
    td_str = str(timedelta(seconds=sec))
    x = td_str.split(':')
    return x[0] + ' Hours ' + x[1] + ' Minutes ' + x[2] + ' Seconds'


def format_text(text: str, list: bool = False, sep: str | None = None, nl: bool = False) -> str:
    result = ""
    if list:
        result += f"★ {text}\n"
    else:
        result += f"{text}\n"

    if sep:
        l = len(result)
        result += sep * (l - 1) + "\n"
    if nl:
        result += "\n"
    return result


def format_key_value(key: str, value: str, list: bool = False, sep: str | None = None, nl: bool = False) -> str:
    result = ""
    if list:
        result += f"★ {key: <13}   →   {value}\n"
    else:
        result += f"{key: <15}   →   {value}\n"
    if sep:
        l = len(result)
        result += sep * (l - 1) + "\n"
    if nl:
        result += "\n"
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


def format_grid(contents: Dict[str, str], info: str):
    result = ""
    info = f"[{info}]"
    count = 0
    for key, (value, col) in contents.items():
        if count % 2 == 0:
            result += f"{info: <8}"
        result += f"{key: <6}"
        result += " → "
        if col == 1:
            result += f"{value: <32}"
            count += 1
        if col == 2:
            result += f"{value: <64}"
            count += 2
        if count % 2 == 0:
            result += "\n"
    if count % 2 == 1:
        result += "\n"
    return result


def format_split(items: List[str], sep="|"):
    result = ""
    for i, item in enumerate(items):
        result += item
        if i != len(items) - 1:
            result += f" {sep} "
    return result
