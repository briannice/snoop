from ui import CustomPacketsUI
from lib.sniffing import getInterfaces


class CustomPacketsView(CustomPacketsUI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Fill interfaces
        self.fill_interfaces(getInterfaces())

    # Fill interfaces in UI combobox
    def fill_interfaces(self, interfaces):
        self.comboBox.clear()
        self.comboBox.addItems(interfaces)
