from PySide6.QtWidgets import QMainWindow

from base.Root import Root


class Window(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set properties of the main window.
        self.setWindowTitle("Snoop")

        # Add root widget to the main window.
        root = Root()
        self.setCentralWidget(root)
