from PyQt5.QtCore import QThreadPool

from models.whois import WhoisLookupResult
from ui import WhoisUi
from utils.validators import ipv4_address_validator
from workers import WhoisLookupWorker


class WhoisView(WhoisUi):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup
        self.thread_pool = QThreadPool.globalInstance()

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
        if not self.validate_input():
            return

        self.is_looking = True
        self.result = None
        self.clear_output()
        self.set_loading()

        domain = self.get_domain()

        worker = WhoisLookupWorker(domain)
        worker.signals.data.connect(self.handler_signal_data)
        self.thread_pool.start(worker)

    def handler_button_clear(self):
        self.result = None
        self.clear_output()
        self.clear_domain_error()

    def handler_signal_data(self, data: WhoisLookupResult):
        text = data.to_text_extended()

        self.is_looking = False
        self.result = text
        self.set_success()
        self.set_output(text)

    # --------------- #
    #    VALIDATORS   #
    # --------------- #

    def validate_input(self) -> bool:
        domain = self.get_domain()
        error = ipv4_address_validator(domain)
        if error is None:
            self.clear_domain_error()
            return True
        self.set_domain_error(error)
        return False
