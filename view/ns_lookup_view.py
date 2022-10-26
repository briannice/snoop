import dns.rdatatype
import dns.rrset

from PyQt5.QtCore import QThreadPool

from ui import NsLookupUi
from models.ns_lookup import NsLookupResult
from utils.validators import domain_name_validator
from workers import NsLookupWorker


class NsLookupView(NsLookupUi):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup
        self.thead_pool = QThreadPool.globalInstance()

        # Data
        self.is_looking: bool = False
        self.result: str | None = None

        # Handlers
        self.get_button_lookup().clicked.connect(self.handler_button_lookup)
        self.get_button_clear().clicked.connect(self.handler_button_clear)

    # ------------- #
    #    HANDLERS   #
    # ------------- #

    def handler_button_lookup(self):
        if self.is_looking:
            return
        if not self.validate():
            return

        self.is_looking = True
        self.result = None
        self.clear_output()
        self.set_loading()

        domain = self.get_domain()
        records = self.get_records()

        worker = NsLookupWorker(domain, records)
        worker.signals.data.connect(self.handler_signal_data)
        self.thead_pool.start(worker)

    def handler_button_clear(self):
        self.result = None
        self.clear_output()
        self.clear_errors()

    def handler_signal_data(self, data: NsLookupResult):
        text = data.to_text_extended()

        self.is_looking = False
        self.result = text
        self.set_success()
        self.set_output(text)

    # --------------- #
    #    VALIDATORS   #
    # --------------- #

    def validate(self) -> bool:
        v1 = self.validate_domain()
        v2 = self.validate_records()
        return v1 and v2

    def validate_domain(self) -> bool:
        domain = self.get_domain()
        error = domain_name_validator(domain)
        if error is None:
            self.clear_domain_error()
            return True
        self.set_domain_error(error)
        return False

    def validate_records(self) -> bool:
        for _, value in self.get_records().items():
            if value:
                self.clear_records_error()
                return True
        self.set_records_error("At least one record should be selected")
        return False
