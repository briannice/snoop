from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.root_widget import RootWidget
import sys
sys.setrecursionlimit(10000)


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
