from typing import Dict
from PyQt5.QtCore import QRunnable, pyqtSlot

from lib.ns_lookup import ns_lookup_records
from signals import NsLookupSignal


class NsLookupWorker(QRunnable):

    def __init__(self, domain: str, records: Dict[str, bool], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.domain = domain
        self.records = records

        self.signals = NsLookupSignal()

    @pyqtSlot()
    def run(self):
        lookup = ns_lookup_records(self.domain, self.records)
        self.signals.data.emit(lookup)
