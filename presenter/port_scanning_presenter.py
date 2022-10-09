from model import PortScanningModel
from view import PortScanningView


class PortScanningPresenter():

    def __init__(self, view: PortScanningView, model: PortScanningModel):
        self.__view = view
        self.__model = model

        self.__add_event_handlers()
        self.__update_view()

    def __add_event_handlers(self):
        pass

    def __update_view(self):
        pass
