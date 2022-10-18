from widgets import ButtonWidget, HLineWidget, LabelWidget, TabWidget, TextWidget
from widgets.input import CheckboxInputWidget, TextInputWidget
from widgets.layout import GLayoutWidget, HLayoutWidget, VLayoutWidget


class PortScanningUi(TabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Select host and ports
        self.SelectHostLabel = LabelWidget("Host", type="label")
        self.SelectHostTextInput = TextInputWidget()
        self.SelectHostError = LabelWidget("", type="error")

        self.SelectPortLabel = LabelWidget("Port", type="label")
        self.SelectPortTextInput = TextInputWidget()
        self.SelectPortError = LabelWidget("", type="error")

        self.SelectHostLayout = GLayoutWidget(h_spacing="sm", v_spacing="sm")
        self.SelectHostLayout.addWidget(self.SelectHostLabel, 0, 0, 1, 1)
        self.SelectHostLayout.addWidget(self.SelectHostTextInput, 0, 1, 1, 1)
        self.SelectHostLayout.addWidget(self.SelectHostError, 1, 0, 1, 2)
        self.SelectHostLayout.addWidget(self.SelectPortLabel, 2, 0, 1, 1)
        self.SelectHostLayout.addWidget(self.SelectPortTextInput, 2, 1, 1, 1)
        self.SelectHostLayout.addWidget(self.SelectPortError, 3, 0, 1, 2)

        # Select Packets
        self.SelectPacketsTitle = LabelWidget("Packets", type="section")
        self.SelectPacketsError = LabelWidget("", type="error")

        self.SelectPacketsStealthLabel = LabelWidget("Stealth")
        self.SelectPacketsConnectLabel = LabelWidget("Connect")
        self.SelectPacketsXmasLabel = LabelWidget("Xmas")
        self.SelectPacketsFinLabel = LabelWidget("FIN")
        self.SelectPacketsAckLabel = LabelWidget("ACK")

        self.SelectPacketsStealthCheckbox = CheckboxInputWidget()
        self.SelectPacketsConnectCheckbox = CheckboxInputWidget()
        self.SelectPacketsXmasCheckbox = CheckboxInputWidget()
        self.SelectPacketsFinCheckbox = CheckboxInputWidget()
        self.SelectPacketsAckCheckbox = CheckboxInputWidget()

        self.SelectPacketsLayout = GLayoutWidget(v_spacing="sm")
        self.SelectPacketsLayout.addWidget(self.SelectPacketsStealthLabel, 0, 0)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsConnectLabel, 0, 1)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsXmasLabel, 0, 2)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsFinLabel, 0, 3)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsAckLabel, 0, 4)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsStealthCheckbox, 1, 0)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsConnectCheckbox, 1, 1)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsXmasCheckbox, 1, 2)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsFinCheckbox, 1, 3)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsAckCheckbox, 1, 4)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsError, 2, 0, 1, 4)

        # Output
        self.OutputText = TextWidget()

        self.OutputTextLayout = VLayoutWidget()
        self.OutputTextLayout.addWidget(self.OutputText)

        # Buttons
        self.ButtonScan = ButtonWidget("Start scan")
        self.ButtonClear = ButtonWidget("Clear output")

        self.ButtonsLayout = HLayoutWidget()
        self.ButtonsLayout.addWidget(self.ButtonScan)
        self.ButtonsLayout.addWidget(self.ButtonClear)

        # Self
        self.Layout = VLayoutWidget()
        self.Layout.addLayout(self.SelectHostLayout)
        self.Layout.addWidget(HLineWidget())
        self.Layout.addLayout(self.SelectPacketsLayout)
        self.Layout.addWidget(HLineWidget())
        self.Layout.addLayout(self.OutputTextLayout)
        self.Layout.addLayout(self.ButtonsLayout)

        self.setLayout(self.Layout)
