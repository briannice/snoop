from widgets import ButtonWidget, HLineWidget, LabelWidget, TabWidget, TextWidget
from widgets.input import CheckboxInputWidget, TextInputWidget
from widgets.layout import GLayoutWidget, HLayoutWidget, VLayoutWidget


class NslookupUi(TabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Domain input
        self.NsLabel = LabelWidget("Domain:")
        self.DomainEdit = TextInputWidget()
        self.DomainButton = ButtonWidget("Scan")

        self.Header = HLayoutWidget()
        self.Header.addWidget(self.NsLabel)
        self.Header.addWidget(self.DomainEdit)
        self.Header.addWidget(self.DomainButton)

        # Options
        self.CheckAllButton = ButtonWidget("Check all")
        self.UncheckAllButton = ButtonWidget("Uncheck all")

        self.CheckButtons = HLayoutWidget()
        self.CheckButtons.addWidget(self.CheckAllButton)
        self.CheckButtons.addWidget(self.UncheckAllButton)

        self.Checkboxes = [CheckboxInputWidget("NS"), CheckboxInputWidget("A"), CheckboxInputWidget("AAAA"),
                           CheckboxInputWidget("MX"), CheckboxInputWidget("SOA")]

        self.CheckBoxInput = HLayoutWidget()
        for x in range(len(self.Checkboxes)):
            self.CheckBoxInput.addWidget(self.Checkboxes[x])

        # Search result
        self.Result = TextWidget()

        self.Resultoutput = VLayoutWidget()
        self.Resultoutput.addWidget(self.Result)

        # Layout of all components
        self.Layout = VLayoutWidget()
        self.Layout.addLayout(self.Header)
        self.Layout.addWidget(HLineWidget())
        self.Layout.addLayout(self.CheckButtons)
        self.Layout.addLayout(self.CheckBoxInput)
        self.Layout.addWidget(HLineWidget())
        self.Layout.addLayout(self.Resultoutput)

        self.setLayout(self.Layout)
