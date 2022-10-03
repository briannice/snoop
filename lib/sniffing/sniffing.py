import argparse, psutil
from scapy.all import *
from psutil._compat import basestring
from scapy.all import *
from scapy.modules.six import StringIO


class Sniffer:

    # Get every interface from host
    def getInterfaces(self):
        adresses = psutil.net_if_addrs()
        return list(adresses.keys())

    def handler(packet):
        return packet.summary()

    def sniffAllPackets(self, interface):
        sniff(iface=interface, prn=lambda x: x.summary(), store=0)
