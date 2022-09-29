from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout


class HomeTab(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Label = QLabel("Home")
        self.Layout = QGridLayout()
        self.Layout.addWidget(self.Label)
        self.setLayout(self.Layout)
