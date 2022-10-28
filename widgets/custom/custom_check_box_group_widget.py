from PyQt5.QtCore import Qt
from typing import Dict, List

from widgets.base import BaseCheckBoxWidget, BaseGridLayoutWidget, BaseGroupBoxWidget, BaseLabelWidget, BaseVBoxLayoutWidget


class CustomCheckBoxGroupWidget(BaseGroupBoxWidget):

    def __init__(self, name: str, labels: List[str]):
        super().__init__()

        # Widgets
        self.col = BaseVBoxLayoutWidget(spacing="lg")
        self.grid = BaseGridLayoutWidget(h_spacing="lg", v_spacing="sm")
        self.name = BaseLabelWidget(type="subtitle", text=name)
        self.error = BaseLabelWidget(type="error")
        self.labels = [BaseLabelWidget(type="label", text=label) for label in labels]
        self.checkboxes = [BaseCheckBoxWidget() for _ in labels]

        # Layout
        self.col.addWidget(self.name)
        for i, label in enumerate(self.labels):
            self.grid.addWidget(label, 1, i)
        for i, checkbox in enumerate(self.checkboxes):
            self.grid.addWidget(checkbox, 2, i)
        self.col.addLayout(self.grid)
        self.setLayout(self.col)

        # Styling
        self.grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        for label in self.labels:
            label.setFixedWidth(100)
        for checkbox in self.checkboxes:
            checkbox.setFixedWidth(100)

    def set_error(self, error):
        self.error.setText(error)
        self.grid.addWidget(self.error, 3, 0, 1, 3)

    def remove_error(self):
        self.error.setText("")
        self.grid.removeWidget(self.error)

    def get_checkbox_value(self, label: str) -> bool:
        i = 0
        for l in self.labels:
            if l.text().lower() == label:
                break
            i += 1
        return self.checkboxes[i].isChecked()

    def get_checkbox_values(self) -> Dict[str, bool]:
        values = {}
        for label, checkbox in zip(self.labels, self.checkboxes):
            values[label.text().lower()] = checkbox.isChecked()
        return values

    def get_checkbox_widgets(self):
        return self.checkboxes
