from PyQt5 import Qt
from widgets import TabWidget


class HomeUI(TabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(Qt.Qt.WA_StyledBackground, True)
        stylesheet = """
                 background-image: url("ui/static/snoop.png");
                background-repeat: no-repeat; 
                background-position: center;
        """
        self.setStyleSheet(stylesheet)
