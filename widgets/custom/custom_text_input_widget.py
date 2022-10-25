from widgets.base import BaseGridLayoutWidget, BaseLabelWidget, BaseLineEditWidget


class CustomTextInputWidget(BaseGridLayoutWidget):

    def __init__(self, name: str, help: str):
        super().__init__(h_spacing="lg", v_spacing="sm")

        # Widgets
        self.input = BaseLineEditWidget()
        self.label = BaseLabelWidget(type="label", text=name)
        self.help = BaseLabelWidget(type="help", text=help)
        self.error = BaseLabelWidget(type="error")

        # Layout
        self.addWidget(self.label, 0, 0)
        self.addWidget(self.input, 0, 1)
        self.addWidget(self.help, 0, 2)

        # Styling
        self.input.setFixedWidth(500)
        self.label.setFixedWidth(50)

    def set_error(self, error):
        self.error.setText(error)
        self.addWidget(self.error, 1, 0, 1, 3)

    def remove_error(self):
        self.error.setText("")
        self.removeWidget(self.error)

    def get_text(self) -> str:
        return self.input.text()
