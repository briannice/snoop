from PyQt5.QtCore import QRunnable, pyqtSlot

from lib.whois_search import whoisQuery
from signals import WhoisLookupSignal


class WhoisLookupWorker(QRunnable):
    def __init__(self, domain: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.domain = domain

        self.signals = WhoisLookupSignal()

    @pyqtSlot()
    def run(self):
        lookup = whoisQuery(self.domain)
        self.signals.data.emit(lookup)
