import argparse, psutil
from scapy.all import *
from psutil._compat import basestring
from scapy.all import *
from scapy.modules.six import StringIO


# Get every interface from host
def getInterfaces():
    adr = psutil.net_if_addrs()
    return list(adr.keys())


def sniffAllPackets(interface, prn):
    sniff(iface=interface, prn=prn, store=0)
