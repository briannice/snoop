from typing import Dict
from widgets.base import BaseGridLayoutWidget, BaseLabelWidget, BaseListWidget, BasePushButtonWidget, BaseTabWidget, BaseTextBrowserWidget
from widgets.custom import CustomCheckBoxGroupWidget, CustomContentDialogWidget, CustomTextInputWidget


class NsLookupUi(BaseTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Widgets
        self.title = BaseLabelWidget(type="title", text="NS lookup")
        self.info = BaseLabelWidget(type="info", align="r")
        self.domain = CustomTextInputWidget("Domain", "Example: www.google.com")
        self.records = CustomCheckBoxGroupWidget("Records", ["NS", "A", "AAAA", "MX", "SOA"])
        self.output = BaseTextBrowserWidget()
        self.button_lookup = BasePushButtonWidget("Start lookup")
        self.button_clear = BasePushButtonWidget("Clear output")

        # Layout
        self.grid = BaseGridLayoutWidget()
        self.grid.addWidget(self.title, 0, 0, 1, 1)
        self.grid.addWidget(self.info, 0, 1, 1, 1)
        self.grid.addLayout(self.domain, 1, 0, 1, 2)
        self.grid.addWidget(self.records, 2, 0, 1, 2)
        self.grid.addWidget(self.output, 3, 0, 1, 2)
        self.grid.addWidget(self.button_lookup, 4, 0, 1, 1)
        self.grid.addWidget(self.button_clear, 4, 1, 1, 1)
        self.setLayout(self.grid)

    def get_domain(self) -> str:
        return self.domain.get_text()

    def get_records(self) -> Dict[str, bool]:
        return self.records.get_checkbox_values()

    def get_output(self) -> BaseTextBrowserWidget:
        return self.output

    def get_button_lookup(self) -> BasePushButtonWidget:
        return self.button_lookup

    def get_button_clear(self) -> BasePushButtonWidget:
        return self.button_clear

    def set_loading(self):
        self.info.set_info()
        self.info.setText("Looking...")

    def set_success(self):
        self.info.set_success()
        self.info.setText("Lookup done!")

    def set_error(self, error: str):
        self.info.set_error()
        self.info.setText(error)

    def set_domain_error(self, error: str):
        self.domain.set_error(error)

    def set_records_error(self, error: str):
        self.records.set_error(error)

    def set_output(self, text: str):
        self.output.setText(text)

    def clear_domain_error(self):
        self.domain.remove_error()

    def clear_records_error(self):
        self.records.remove_error()

    def clear_errors(self):
        self.clear_domain_error()
        self.clear_records_error()

    def clear_output(self):
        self.output.clear()
