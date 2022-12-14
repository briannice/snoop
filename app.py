import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

from view import RootView


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(1010, 840)

        root_view = RootView()

        self.setWindowTitle("Snoop - Network analyzer and hacking tool ©KDG")
        self.setWindowIcon(QtGui.QIcon('static/snoop_logo_256x256.png'))
        self.setContentsMargins(5, 5, 5, 5)
        self.setCentralWidget(root_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    status = app.exec()
    sys.exit(status)
