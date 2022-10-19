from widgets import ButtonWidget, GroupWidget, HLineWidget, LabelWidget, TabWidget, TextWidget
from widgets.input import CheckboxInputWidget, TextInputWidget
from widgets.layout import GLayoutWidget, HLayoutWidget, VLayoutWidget


class PortScanningUi(TabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Title
        self.Title = LabelWidget("Port scanning", type="title")

        # Select host and ports
        self.SelectHostLabel = LabelWidget("Host", type="label")
        self.SelectHostTextInput = TextInputWidget()
        self.SelectHostError = LabelWidget("This is an error!", type="error")
        self.SelectHostInfo = LabelWidget("Example: 192.168.56.1", type="info")

        self.SelectPortLabel = LabelWidget("Port", type="label")
        self.SelectPortTextInput = TextInputWidget()
        self.SelectPortError = LabelWidget("This is an error!", type="error")
        self.SelectPortInfo = LabelWidget("Using individual ports: 22,23,80\nUsing ranges: 22-24,80", type="info")

        self.SelectHostLayout = GLayoutWidget(h_spacing="sm", v_spacing="sm")
        self.SelectHostLayout.addWidget(self.SelectHostLabel, 0, 0, 1, 1)
        self.SelectHostLayout.addWidget(self.SelectHostTextInput, 0, 1, 1, 1)
        self.SelectHostLayout.addWidget(self.SelectHostInfo, 0, 2, 1, 1)
        self.SelectHostLayout.addWidget(self.SelectHostError, 1, 0, 1, 2)
        self.SelectHostLayout.addWidget(self.SelectPortLabel, 2, 0, 1, 1)
        self.SelectHostLayout.addWidget(self.SelectPortTextInput, 2, 1, 1, 1)
        self.SelectHostLayout.addWidget(self.SelectPortError, 3, 0, 1, 2)
        self.SelectHostLayout.addWidget(self.SelectPortInfo, 2, 2, 1, 1)

        # Select Packets
        self.SelectPacketsError = LabelWidget("This is an error!", type="error")

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

        self.SelectPacketsGroup = GroupWidget("Packets")
        self.SelectPacketsGroup.setLayout(self.SelectPacketsLayout)

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
        self.Layout.addWidget(self.Title)
        self.Layout.addLayout(self.SelectHostLayout)
        self.Layout.addWidget(self.SelectPacketsGroup)
        self.Layout.addLayout(self.OutputTextLayout)
        self.Layout.addLayout(self.ButtonsLayout)

        self.setLayout(self.Layout)

    def get_packet_checkboxes(self):
        return [
            self.SelectPacketsAckCheckbox,
            self.SelectPacketsConnectCheckbox,
            self.SelectPacketsStealthCheckbox,
            self.SelectPacketsFinCheckbox,
            self.SelectPacketsXmasCheckbox
        ]
