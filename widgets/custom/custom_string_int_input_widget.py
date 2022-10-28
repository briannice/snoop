from widgets.base import BaseHBoxLayoutWidget, BaseLabelWidget, BaseLineEditWidget, BaseVBoxLayoutWidget


class CustomStringIntInputWidget(BaseVBoxLayoutWidget):

    def __init__(self, label_str: str, label_int: str, help: str = ""):
        super().__init__()

        # Widgets
        self.str_label = BaseLabelWidget(type="label", text=label_str)
        self.int_label = BaseLabelWidget(type="label", text=label_int)
        self.str = BaseLineEditWidget()
        self.int = BaseLineEditWidget()
        self.help = BaseLabelWidget(type="help", text=help)
        self.row = BaseHBoxLayoutWidget()
        self.error = BaseLabelWidget(type="error")

        # Layout
        self.row.addWidget(self.str_label)
        self.row.addWidget(self.str)
        self.row.addSpacing(40)
        self.row.addWidget(self.int_label)
        self.row.addWidget(self.int)
        self.row.addSpacing(40)
        self.row.addWidget(self.help)
        self.addLayout(self.row)

        # Styling
        self.str.setFixedWidth(300)
        self.int.setFixedWidth(100)
        self.str_label.setFixedWidth(120)
        self.int_label.setFixedWidth(120)

    def set_error(self, error):
        self.error.setText(error)
        self.addWidget(self.error)

    def remove_error(self):
        self.error.setText("")
        self.removeWidget(self.error)

    def set_label_str(self, text: str):
        self.str_label.setText(text)

    def set_label_int(self, text: str):
        self.int_label.setText(text)

    def get_str(self) -> str:
        return self.str.text()

    def get_int(self) -> str:
        return self.int.text()
