from typing import Dict
from dns import name, rdatatype, message, query, rdataclass

from models.ns_lookup import NsLookupResult


def ns_lookup_records(domain: str, records: Dict[str, bool]):
    result = NsLookupResult()
    for record, value in records.items():
        if value:
            record = record.upper()
            lookup = ns_lookup_record(domain, record)
            result.add_record(record, lookup)
    return result


def ns_lookup_record(domain: str, search_type: str):
    search_type = rdatatype.from_text(search_type)
    qdomain = name.from_text(domain)
    q = message.make_query(qdomain, search_type)
    # todo: maybe add to choose DNS server instead of 8.8.8.8?
    r = query.udp(q, "8.8.8.8")
    try:
        ns_rrset = r.find_rrset(r.answer, qdomain, rdataclass.IN, search_type)
        return ns_rrset
    except:
        return None
