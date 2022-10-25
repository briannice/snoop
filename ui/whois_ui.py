from widgets import TabWidget, LabelWidget, ButtonWidget, HLineWidget, TextWidget
from widgets.input import TextInputWidget
from widgets.layout import HLayoutWidget, VLayoutWidget


class WhoisUi(TabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Domain input
        self.WhoisLabel = LabelWidget("Domain:")
        #todo: change domain to "domain or IP"
        self.DomainEdit = TextInputWidget()
        self.DomainButton = ButtonWidget("Search")

        self.Header = HLayoutWidget()
        self.Header.addWidget(self.WhoisLabel)
        self.Header.addWidget(self.DomainEdit)
        self.Header.addWidget(self.DomainButton)

        # Search result
        self.Result = TextWidget()

        self.Resultoutput = VLayoutWidget()
        self.Resultoutput.addWidget(self.Result)

        # Layout of all components
        self.Layout = VLayoutWidget()
        self.Layout.addLayout(self.Header)
        self.Layout.addWidget(HLineWidget())
        self.Layout.addLayout(self.Resultoutput)

        self.setLayout(self.Layout)