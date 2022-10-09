from PyQt5.QtCore import QThreadPool

from model import NetworkScanningModel
from view import NetworkScanningView
from worker import NetworkScanningWorker


class NetworkScanningPresenter():

    def __init__(self, view: NetworkScanningView, model: NetworkScanningModel):
        self.__view = view
        self.__model = model

        self.__add_event_handlers()
        self.__update_view()

    def __add_event_handlers(self):
        self.__view.get_button_scan().clicked.connect(self.__button_scan_handler)

    def __button_scan_handler(self):
        print("Start worker")
        worker = NetworkScanningWorker()
        QThreadPool.globalInstance().start(worker)

    def __update_view(self):

        # Set all checkboxes for packet selection to True
        for cb in self.__view.get_select_packets_checkboxes():
            cb.setChecked(True)
