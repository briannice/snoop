from widgets import ButtonWidget, HLineWidget, LabelWidget, TabWidget, TextWidget
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

        # Filter
        self.FilterUpLabel = LabelWidget("UP")
        self.FilterUnknownLabel = LabelWidget("UNKNOWN")
        self.FilterBlockedLabel = LabelWidget("BLOCKED")
        self.FilteSpacerLabel = LabelWidget("")

        self.FilterUpCheckbox = CheckboxInputWidget()
        self.FilterUnknownCheckbox = CheckboxInputWidget()
        self.FilterBlockedCheckbox = CheckboxInputWidget()

        self.FilterLayout = GLayoutWidget()
        self.FilterLayout.addWidget(self.FilterUpLabel, 0, 0)
        self.FilterLayout.addWidget(self.FilterUnknownLabel, 0, 1)
        self.FilterLayout.addWidget(self.FilterBlockedLabel, 0, 2)
        self.FilterLayout.addWidget(self.FilteSpacerLabel, 0, 3)
        self.FilterLayout.addWidget(self.FilterUpCheckbox, 1, 0)
        self.FilterLayout.addWidget(self.FilterUnknownCheckbox, 1, 1)
        self.FilterLayout.addWidget(self.FilterBlockedCheckbox, 1, 2)

        # Result
        self.OutputText = TextWidget()

        self.OutputLayout = VLayoutWidget()
        self.OutputLayout.addWidget(self.OutputText)

        # Buttons
        self.ButtonScan = ButtonWidget("Start scan")
        self.ButtonClear = ButtonWidget("Clear output")

        self.ButtonsLayout = HLayoutWidget()
        self.ButtonsLayout.addWidget(self.ButtonScan)
        self.ButtonsLayout.addWidget(self.ButtonClear)

        # Self
        self.Layout = VLayoutWidget()
        self.Layout.addLayout(self.SelectNetworkLayout)
        self.Layout.addWidget(HLineWidget())
        self.Layout.addLayout(self.SelectPacketsLayout)
        self.Layout.addWidget(HLineWidget())
        self.Layout.addLayout(self.FilterLayout)
        self.Layout.addLayout(self.OutputLayout)
        self.Layout.addLayout(self.ButtonsLayout)

        # Setup
        self.setLayout(self.Layout)
