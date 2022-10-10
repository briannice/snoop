from widgets import ButtonWidget, HLineWidget, LabelWidget, TabWidget
from widgets.input import CheckboxInputWidget, TextInputWidget
from widgets.layout import GLayoutWidget, HLayoutWidget, VLayoutWidget


class NetworkScanningUi(TabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Select network
        self.SelectNetworkLabel = LabelWidget("Network")
        self.SelectNetworkTextInput = TextInputWidget()

        self.SelectNetworkLayout = HLayoutWidget()
        self.SelectNetworkLayout.addWidget(self.SelectNetworkLabel)
        self.SelectNetworkLayout.addWidget(self.SelectNetworkTextInput)

        # Select packets
        self.SelectPacketsPingLabel = LabelWidget("Ping")
        self.SelectPacketsSshLabel = LabelWidget("SSH")
        self.SelectPacketsHttpLabel = LabelWidget("HTTP")
        self.SelectPacketsHttpsLabel = LabelWidget("HTTPS")

        self.SelectPacketsPingCheckbox = CheckboxInputWidget()
        self.SelectPacketsSshCheckbox = CheckboxInputWidget()
        self.SelectPacketsHttpCheckbox = CheckboxInputWidget()
        self.SelectPacketsHttpsCheckbox = CheckboxInputWidget()

        self.SelectPacketsLayout = GLayoutWidget()
        self.SelectPacketsLayout.addWidget(self.SelectPacketsPingLabel, 0, 0)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsSshLabel, 0, 1)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsHttpLabel, 0, 2)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsHttpsLabel, 0, 3)

        self.SelectPacketsLayout.addWidget(self.SelectPacketsPingCheckbox, 1, 0)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsSshCheckbox, 1, 1)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsHttpCheckbox, 1, 2)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsHttpsCheckbox, 1, 3)

        # Buttons
        self.ButtonScan = ButtonWidget("Start scan")
        self.ButtonClear = ButtonWidget("Clear output")

        self.ButtonsLayout = HLayoutWidget()
        self.ButtonsLayout.addWidget(self.ButtonScan)
        self.ButtonsLayout.addWidget(self.ButtonClear)

        # Result
        self.OutputLayout = VLayoutWidget()

        # Self
        self.Layout = VLayoutWidget()
        self.Layout.addLayout(self.SelectNetworkLayout)
        self.Layout.addWidget(HLineWidget())
        self.Layout.addLayout(self.SelectPacketsLayout)
        self.Layout.addWidget(HLineWidget())
        self.Layout.addLayout(self.ButtonsLayout)
        self.Layout.addLayout(self.OutputLayout)

        # Setup
        self.setLayout(self.Layout)
