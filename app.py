import sys

from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Snoop")
        self.setMinimumSize(800, 600)
        self.setContentsMargins(5, 5, 5, 5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    status = app.exec()
    sys.exit(status)
