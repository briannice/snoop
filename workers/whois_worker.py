from PyQt5.QtCore import QRunnable, pyqtSlot

from lib.whois import whois_query
from signals import WhoisSignal


class WhoisWorker(QRunnable):
    def __init__(self, domain: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.domain = domain

        self.signals = WhoisSignal()

    @pyqtSlot()
    def run(self):
        lookup = whois_query(self.domain)
        self.signals.data.emit(lookup)
