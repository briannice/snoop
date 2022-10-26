from PyQt5 import Qt
from widgets.base import BaseTabWidget


class HomeUI(BaseTabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(Qt.Qt.WA_StyledBackground, True)
        self.setStyleSheet("""
            background-image: url("static/snoop.png");
            background-repeat: no-repeat; 
            background-position: center;
        """)
