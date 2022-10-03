import dns.resolver
import dns.message
import dns.rdataclass
import dns.rdatatype
import dns.query


def lookupRecord(domain, searchType: dns.rdatatype.RdataType):
    qdomain = dns.name.from_text(domain)
    q = dns.message.make_query(qdomain, searchType)
    # todo: maybe add to choose DNS server instead of 8.8.8.8?
    r = dns.query.udp(q, "8.8.8.8")
    try:
        ns_rrset = r.find_rrset(r.answer, qdomain, dns.rdataclass.IN, searchType)
        pass
    except:
        return None
    return ns_rrset
