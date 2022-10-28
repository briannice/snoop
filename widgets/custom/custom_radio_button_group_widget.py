from PyQt5.QtCore import Qt

from typing import List
from widgets.base import BaseGridLayoutWidget, BaseGroupBoxWidget, BaseLabelWidget, BaseRadioButtonWidget, BaseVBoxLayoutWidget


class CustomRadioButtonGroupWidget(BaseGroupBoxWidget):

    def __init__(self, name: str, labels: List[str]):
        super().__init__()

        self.col = BaseVBoxLayoutWidget(spacing="lg")
        self.grid = BaseGridLayoutWidget(h_spacing="lg", v_spacing="sm")
        self.name = BaseLabelWidget(type="subtitle", text=name)
        self.labels = [BaseLabelWidget(type="label", text=label) for label in labels]
        self.radios = [BaseRadioButtonWidget() for _ in labels]

        # Layout
        self.col.addWidget(self.name)
        for i, label in enumerate(self.labels):
            self.grid.addWidget(label, 1, i)
        for i, checkbox in enumerate(self.radios):
            self.grid.addWidget(checkbox, 2, i)
        self.col.addLayout(self.grid)
        self.setLayout(self.col)

        # Styling
        self.grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        for label in self.labels:
            label.setFixedWidth(100)
        for radio in self.radios:
            radio.setFixedWidth(100)
        self.radios[0].setChecked(True)

    def get_value(self) -> str:
        for i, radio in enumerate(self.radios):
            if radio.isChecked():
                return self.labels[i].text()

    def get_radio_buttons(self) -> List[BaseRadioButtonWidget]:
        return self.radios
