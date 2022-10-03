import ipaddress


from ipaddress import IPv4Network


def network_scan(
    network: IPv4Network = IPv4Network("192.168.1.1/24"),
    ping: bool = True,
):
    pass
