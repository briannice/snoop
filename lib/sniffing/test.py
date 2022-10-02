from psutil._compat import basestring
from scapy.all import *
from scapy.modules.six import StringIO


def handler(packet):
    print(packet.summary())

    # Redirect output of print to variable 'capture'
    capture = StringIO()
    save_stdout = sys.stdout
    sys.stdout = capture
    packet.show()
    sys.stdout = save_stdout

    # capture.getvalue() is a string with the output of 'pack.show()'
    #print(capture.getvalue())

    # Verify that capture.getvalue() is a string
    #print(isinstance(capture.getvalue(), basestring))


if __name__ == "__main__":
    sniff(iface="Ethernet", prn=handler, store=0)