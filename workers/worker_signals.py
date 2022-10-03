from PyQt5.QtCore import pyqtSignal, QObject


class WorkerSignals(QObject):
    """
    Represents the signals between the main thread and a worker thread.
    

    Attributes
    ==========

    * finished (Signal[bool]): signal to indicate that the process is finished.

    * progress (Signal[int]): signal to stream the progress of the thread.

    * result (Signal[object]): signal to stream the result of the thread.

    """
    
    finished = pyqtSignal(bool)
    progress = pyqtSignal(int)
    result = pyqtSignal(object)