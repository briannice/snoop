import sys

import dns.rdatatype
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

from ui import RootWidget


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Snoop")

        self.RootWidget = RootWidget()
        self.setCentralWidget(self.RootWidget)


# testing, will delete later
from lib.domainresearch.nslookup import *

res = lookupRecord("kdg.be", dns.rdatatype.AAAA)
if res is not None:
    for re in res:
        if re.rdtype == dns.rdatatype.MX:
            print(re.exchange)
        else:
            print(re)
else:
    print("No records found")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    status = app.exec()
    sys.exit(status)
