from ipwhois import IPWhois

from models.whois import WhoisLookupResult


def whois_query(ip: str):
    result = WhoisLookupResult()
    query = IPWhois(ip)
    out = query.lookup_rdap(asn_methods=['whois'])
    result.build_search_result(out)
    return result
