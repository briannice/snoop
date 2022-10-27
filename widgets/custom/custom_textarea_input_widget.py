from PyQt5.QtCore import Qt
from widgets.base import BaseGridLayoutWidget, BaseLabelWidget, BasePlaneTextEditWidget


class CustomTextareaInputWidget(BaseGridLayoutWidget):

    def __init__(self, name: str, help: str):
        super().__init__(h_spacing="lg", v_spacing="sm")

        # Widgets
        self.label = BaseLabelWidget(type="label", text=name)
        self.input = BasePlaneTextEditWidget()
        self.help = BaseLabelWidget(type="help", text=help)
        self.error = BaseLabelWidget(type="error")

        # Layout
        self.addWidget(self.label, 0, 0, 1, 1)
        self.addWidget(self.help, 0, 1, 1, 1)
        self.addWidget(self.input, 1, 0, 1, 2)

    def set_error(self, error):
        self.error.setText(error)
        self.addWidget(self.error, 2, 0, 1, 2)

    def remove_error(self):
        self.error.setText("")
        self.removeWidget(self.error)

    def get_text(self) -> str:
        return self.input.toPlainText()
