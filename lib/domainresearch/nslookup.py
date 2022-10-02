import dns.resolver
import dns.message
import dns.rdataclass
import dns.rdatatype
import dns.query


def lookupNsRecord(domain):
    qdomain = dns.name.from_text(domain)
    q = dns.message.make_query(qdomain, dns.rdatatype.NS)
    # todo: maybe add to choose DNS server instead of 8.8.8.8?
    r = dns.query.udp(q, "8.8.8.8")
    ns_rrset = r.find_rrset(r.answer, qdomain, dns.rdataclass.IN, dns.rdatatype.NS)
    return ns_rrset
