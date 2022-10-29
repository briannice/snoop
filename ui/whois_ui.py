from widgets.base import BaseTabWidget, BaseLabelWidget, BaseGridLayoutWidget, BaseTextBrowserWidget, \
    BasePushButtonWidget
from widgets.custom import CustomTextInputWidget


class WhoisUi(BaseTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Widgets
        self.title = BaseLabelWidget(type="title", text="Whois lookup")
        self.info = BaseLabelWidget(type="info", align="r")
        self.domain = CustomTextInputWidget("Domain", "Example: 104.16.208.90")
        self.output = BaseTextBrowserWidget()
        self.button_lookup = BasePushButtonWidget("Start lookup")
        self.button_clear = BasePushButtonWidget("Clear output")

        # Layout
        self.grid = BaseGridLayoutWidget()
        self.grid.addWidget(self.title, 0, 0, 1, 1)
        self.grid.addWidget(self.info, 0, 1, 1, 1)
        self.grid.addLayout(self.domain, 1, 0, 1, 2)
        self.grid.addWidget(self.output, 2, 0, 1, 2)
        self.grid.addWidget(self.button_lookup, 3, 0, 1, 1)
        self.grid.addWidget(self.button_clear, 3, 1, 1, 1)

        self.setLayout(self.grid)

    def get_domain(self) -> str:
        return self.domain.get_text()

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

    def set_output(self, text: str):
        self.output.setText(text)

    def clear_domain_error(self):
        self.domain.remove_error()

    def clear_output(self):
        self.output.clear()