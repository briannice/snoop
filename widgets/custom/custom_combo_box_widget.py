from widgets.base import BaseGridLayoutWidget, BaseLabelWidget, BaseComboBoxWidget


class CustomComboBoxWidget(BaseGridLayoutWidget):

    def __init__(self, name: str, help: str):
        super().__init__()

        # Widgets
        self.label = BaseLabelWidget(type="label", text=name)
        self.combobox = BaseComboBoxWidget()
        self.help = BaseLabelWidget(type="help", text=help)

        # Layout
        self.addWidget(self.label, 0, 0)
        self.addWidget(self.combobox, 0, 1)
        self.addWidget(self.help, 0, 2)

        # Styling
        self.combobox.setFixedWidth(500)
        self.label.setFixedWidth(80)

    def clear(self):
        self.combobox.clear()

    def add_item(self, item: str):
        self.combobox.addItem(item)

    def get_text(self) -> str:
        return self.combobox.currentText()
