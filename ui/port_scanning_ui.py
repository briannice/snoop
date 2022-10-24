from widgets import ButtonWidget, GroupWidget, LabelWidget, ListWidget, TabWidget, TextWidget
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
        self.SelectHostError = LabelWidget("", type="error")
        self.SelectHostInfo = LabelWidget("Example: 192.168.56.1", type="help")

        self.SelectPortLabel = LabelWidget("Ports", type="label")
        self.SelectPortTextInput = TextInputWidget()
        self.SelectPortError = LabelWidget("", type="error")
        self.SelectPortInfo = LabelWidget("Using individual ports: 22,23,80\nUsing ranges: 22-24,80", type="help")

        self.SelectHostLayout = GLayoutWidget(h_spacing="sm", v_spacing="sm")

        self.SelectHostLayout.addWidget(self.SelectHostLabel, 0, 0, 1, 1)
        self.SelectHostLayout.addWidget(self.SelectHostTextInput, 0, 1, 1, 1)
        self.SelectHostLayout.addWidget(self.SelectHostInfo, 0, 2, 1, 1)

        self.SelectHostLayout.addWidget(self.SelectPortLabel, 2, 0, 1, 1)
        self.SelectHostLayout.addWidget(self.SelectPortTextInput, 2, 1, 1, 1)
        self.SelectHostLayout.addWidget(self.SelectPortInfo, 2, 2, 1, 1)

        # Select Packets
        self.SelectPacketsError = LabelWidget("", type="error")

        self.SelectPacketsStealthLabel = LabelWidget("Stealth")
        self.SelectPacketsConnectLabel = LabelWidget("Connect")
        self.SelectPacketsXmasLabel = LabelWidget("Xmas")
        self.SelectPacketsFinLabel = LabelWidget("FIN")
        self.SelectPacketsNullLabel = LabelWidget("NULL")
        self.SelectPacketsAckLabel = LabelWidget("ACK")

        self.SelectPacketsStealthCheckbox = CheckboxInputWidget()
        self.SelectPacketsConnectCheckbox = CheckboxInputWidget()
        self.SelectPacketsXmasCheckbox = CheckboxInputWidget()
        self.SelectPacketsFinCheckbox = CheckboxInputWidget()
        self.SelectPacketsNullCheckbox = CheckboxInputWidget()
        self.SelectPacketsAckCheckbox = CheckboxInputWidget()

        self.SelectPacketsLayout = GLayoutWidget(v_spacing="sm")
        self.SelectPacketsLayout.addWidget(self.SelectPacketsStealthLabel, 0, 0)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsConnectLabel, 0, 1)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsXmasLabel, 0, 2)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsFinLabel, 0, 3)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsNullLabel, 0, 4)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsAckLabel, 0, 5)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsStealthCheckbox, 1, 0)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsConnectCheckbox, 1, 1)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsXmasCheckbox, 1, 2)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsFinCheckbox, 1, 3)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsNullCheckbox, 1, 4)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsAckCheckbox, 1, 5)

        self.SelectPacketsGroup = GroupWidget("Select packets", self.SelectPacketsLayout)

        # Scanning info
        self.ScanningInfoLabel = LabelWidget("", type="info")

        self.ScanningInfoLayout = VLayoutWidget()
        self.ScanningInfoLayout.addWidget(self.ScanningInfoLabel)

        # Output
        self.OutputList = ListWidget()

        self.OutputTextLayout = VLayoutWidget()
        self.OutputTextLayout.addWidget(self.OutputList)

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
        self.Layout.addLayout(self.ScanningInfoLayout)
        self.Layout.addLayout(self.OutputTextLayout)
        self.Layout.addLayout(self.ButtonsLayout)

        self.setLayout(self.Layout)

    def get_packet_checkboxes(self):
        return [
            self.SelectPacketsConnectCheckbox,
            self.SelectPacketsStealthCheckbox,
            self.SelectPacketsFinCheckbox,
            self.SelectPacketsXmasCheckbox,
            self.SelectPacketsAckCheckbox,
            self.SelectPacketsNullCheckbox,
        ]

    def get_packet_checkbox_statuses(self):
        return {
            "ack": self.SelectPacketsAckCheckbox.isChecked(),
            "connect": self.SelectPacketsConnectCheckbox.isChecked(),
            "stealth": self.SelectPacketsStealthCheckbox.isChecked(),
            "fin": self.SelectPacketsFinCheckbox.isChecked(),
            "xmas": self.SelectPacketsXmasCheckbox.isChecked(),
            "null": self.SelectPacketsNullCheckbox.isChecked(),
        }
