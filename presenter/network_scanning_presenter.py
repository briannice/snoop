from model import NetworkScanningModel
from view import NetworkScanningView


class NetworkScanningPresenter():

    def __init__(self, view: NetworkScanningView, model: NetworkScanningModel):
        self.view = view
        self.model = model
        self._add_event_handlers()
        self._update_view()

    def _add_event_handlers(self):
        pass

    def _update_view(self):
        pass
