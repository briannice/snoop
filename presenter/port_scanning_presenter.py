from model import PortScanningModel
from view import PortScanningView


class PortScanningPresenter():

    def __init__(self, view: PortScanningView, model: PortScanningModel):
        self.view = view
        self.model = model
        self._add_event_handlers()
        self._update_view()

    def _add_event_handlers(self):
        pass

    def _update_view(self):
        pass
