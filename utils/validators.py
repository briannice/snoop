def port_validator(text: str) -> str | None:
    if text == "":
        return "Port can not be empty"
    try:
        text = int(text)
    except:
        return "Port must be a number"
    if text < 0:
        return "Port must be a positive number"
    if text > 65535:
        return "Port must be less than 255"
    return None


def icmp_type_validator(text: str) -> str | None:
    if text == "":
        return "ICMP type can not be empty"
    try:
        text = int(text)
    except:
        return "ICMP type must be a number"
    if text < 0:
        return "ICMP type must be a positive number"
    if text > 65535:
        return "ICMP type must be less than 255"
    return None


def icmp_code_validator(text: str) -> str | None:
    if text == "":
        return "ICMP code can not be empty"
    try:
        text = int(text)
    except:
        return "ICMP code must be a number"
    if text < 0:
        return "ICMP code must be a positive number"
    if text > 65535:
        return "ICMP code must be less than 65535"
    return None


def port_range_validator(text: str) -> str | None:
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


def domain_name_validator(domain: str) -> str | None:
    if len(domain) < 2:
        return "Domain must be at least 2 characters"
    if len(domain) > 63:
        return "Domain cannot be more than 63 characters"
    return None


def ipv4_address_validator(domain: str) -> str | None:
    octets = domain.split(".")
    if len(octets) != 4:
        return "Not a valid IPv4 address"
    return None
