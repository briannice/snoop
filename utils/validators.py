def port_input_validator(text: str) -> str | None:
    chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", ","]
    max = 65535
    min = 1

    if text == "":
        return "Ports cannot be empty"

    for c in text:
        if c not in chars:
            "Ports can only contain numbers, '-' and ','"

    for t in text.split(","):
        if t == "":
            "Port range cannot be empty"

        if "," in t:
            "Port range cannot contain ','"

        count = t.count("-")
        if count == 0:
            p = int(t)
            if p < min or p > max:
                "Port range cannot contain ','"
        elif count == 1:
            ps = t.split("-")
            for p in ps:
                p = int(p)
                if p < min or p > max:
                    "Port range cannot contain ','"
        else:
            "Port range can only contain one '-'"

    return None
