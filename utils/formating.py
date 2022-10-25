from .exception import SnoopException


def format_key_value(key: str, value: str, type: str) -> str:
    result = ""
    match type:
        case "group":
            result += f"{key: <12}   →   {value}\n"
            l = len(result)
            result += "=" * l + "\n\n"
        case "title":
            result += f"{key: <12}   →   {value}\n"
            l = len(result)
            result += "-" * l + "\n"
        case "item":
            result += f"★ {key: <10}   →   {value}\n"
        case _:
            raise SnoopException("Invalid formatting type")
    return result


def format_key(key: str, type: str) -> str:
    result = ""
    match type:
        case "group":
            result += f"{key}\n"
            l = len(result)
            result += "-" * l + "\n\n"
        case "title":
            result += f"{key}\n"
            l = len(result)
            result += "-" * l + "\n"
        case "item":
            result += f"★ {key}\n"
        case _:
            raise SnoopException("Invalid formatting type")
    return result
