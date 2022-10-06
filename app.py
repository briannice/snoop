import sys

import dns.rdatatype
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

from ui.root_widget import RootWidget


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Snoop")

        self.RootWidget = RootWidget()
        self.setCentralWidget(self.RootWidget)
        self.setContentsMargins(5, 5, 5, 5)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    status = app.exec()
    sys.exit(status)
