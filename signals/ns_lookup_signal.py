from PyQt5.QtCore import pyqtSignal, QObject


class NsLookupSignal(QObject):
    data = pyqtSignal(object)
