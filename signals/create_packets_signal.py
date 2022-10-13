from PyQt5.QtCore import pyqtSignal, QObject


class CreatePacketSignal(QObject):
    result = pyqtSignal(object)

