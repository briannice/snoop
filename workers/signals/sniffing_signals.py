from PyQt5.QtCore import pyqtSignal, QObject


class WorkerSignals(QObject):
    # Run signal: default = True
    run = pyqtSignal(bool)
    # Data flowing channel
    result = pyqtSignal(object)
