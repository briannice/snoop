from ipwhois import IPWhois

from lib.ns_lookup import lookup_record
import dns.rdatatype


def whois_query(domain):
    octets = domain.split(".")
    ip = None
    if len(octets) != 4:
        # in theory not a IPv4 address, but a domain input
        result = lookup_record(domain, dns.rdatatype.A)
        if result is not None:
            for re in result:
                ip = re

    if ip is not None:
        query = IPWhois(ip)
        out = query.lookup_rdap(asn_methods=['whois'])

        return out

    # todo: eerst checken of domain een IPv4 address of IPv6 is of een domein naam, als
    # als het een IP adres is dan moet er eerst een nslookup gedaan worden naar IP adres en daarna teruggeven om query uit te voeren
    # daarna pas rest van programma laten verlopen
    # --> nog uitvogelen hoe ik het ga aanpakken IPv6 te gebruiken, nu enkel omzetting naar IPv4 bij ingeven domein
