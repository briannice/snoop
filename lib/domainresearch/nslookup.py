import dns.resolver
import dns.message
import dns.rdataclass
import dns.rdatatype
import dns.query


# todo: use of dns.rdatatype.Rdatatypes as parameter

def lookupNsRecord(domain):
    qdomain = dns.name.from_text(domain)
    q = dns.message.make_query(qdomain, dns.rdatatype.NS)
    # todo: maybe add to choose DNS server instead of 8.8.8.8?
    r = dns.query.udp(q, "8.8.8.8")
    try:
        ns_rrset = r.find_rrset(r.answer, qdomain, dns.rdataclass.IN, dns.rdatatype.NS)
        pass
    except:
        return None
    return ns_rrset


def lookupARecord(domain):
    qdomain = dns.name.from_text(domain)
    q = dns.message.make_query(qdomain, dns.rdatatype.A)
    # todo: maybe add to choose DNS server instead of 8.8.8.8?
    r = dns.query.udp(q, "8.8.8.8")
    try:
        ns_rrset = r.find_rrset(r.answer, qdomain, dns.rdataclass.IN, dns.rdatatype.A)
        pass
    except:
        return None
    return ns_rrset


def lookupAAAARecord(domain):
    qdomain = dns.name.from_text(domain)
    q = dns.message.make_query(qdomain, dns.rdatatype.AAAA)
    # todo: maybe add to choose DNS server instead of 8.8.8.8?
    r = dns.query.udp(q, "8.8.8.8")
    try:
        ns_rrset = r.find_rrset(r.answer, qdomain, dns.rdataclass.IN, dns.rdatatype.AAAA)
        pass
    except:
        return None
    return ns_rrset

def lookupMXRecord(domain):
    qdomain = dns.name.from_text(domain)
    q = dns.message.make_query(qdomain, dns.rdatatype.MX)
    # todo: maybe add to choose DNS server instead of 8.8.8.8?
    r = dns.query.udp(q, "8.8.8.8")
    try:
        ns_rrset = r.find_rrset(r.answer, qdomain, dns.rdataclass.IN, dns.rdatatype.MX)
        pass
    except:
        return None
    return ns_rrset
