from PyQt5.QtCore import pyqtSignal, QObject


class CustomPacketSignal(QObject):
    packet = pyqtSignal(object)
