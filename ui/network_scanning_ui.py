from widgets import ButtonWidget, HLineWidget, LabelWidget, TabWidget, TextWidget
from widgets.input import CheckboxInputWidget, TextInputWidget
from widgets.layout import GLayoutWidget, HLayoutWidget, VLayoutWidget


class NetworkScanningUi(TabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Select network
        self.SelectNetworkTitle = LabelWidget("Network", type="section")
        self.SelectNetworkTextInput = TextInputWidget()
        self.SelectNetworkError = LabelWidget("Network invalid!", type="error")

        self.SelectNetworkLayout = VLayoutWidget(spacing="sm")
        self.SelectNetworkLayout.addWidget(self.SelectNetworkTextInput)
        self.SelectNetworkLayout.addWidget(self.SelectNetworkError)

        # Select packets
        self.SelectPacketsTitle = LabelWidget("Packets", type="section")
        self.SelectPacketsError = LabelWidget("", type="error")

        self.SelectPacketsPingLabel = LabelWidget("Ping")
        self.SelectPacketsSshLabel = LabelWidget("SSH")
        self.SelectPacketsHttpLabel = LabelWidget("HTTP")
        self.SelectPacketsHttpsLabel = LabelWidget("HTTPS")

        self.SelectPacketsPingCheckbox = CheckboxInputWidget()
        self.SelectPacketsSshCheckbox = CheckboxInputWidget()
        self.SelectPacketsHttpCheckbox = CheckboxInputWidget()
        self.SelectPacketsHttpsCheckbox = CheckboxInputWidget()

        self.SelectPacketsLayout = GLayoutWidget(v_spacing="sm")
        self.SelectPacketsLayout.addWidget(self.SelectPacketsPingLabel, 0, 0)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsSshLabel, 0, 1)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsHttpLabel, 0, 2)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsHttpsLabel, 0, 3)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsPingCheckbox, 1, 0)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsSshCheckbox, 1, 1)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsHttpCheckbox, 1, 2)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsHttpsCheckbox, 1, 3)
        self.SelectPacketsLayout.addWidget(self.SelectPacketsError, 2, 0, 1, 4)

        # Filter
        self.FilterTitle = LabelWidget("Filter", type="section")
        self.FilterError = LabelWidget("", type="error")

        self.FilterUpLabel = LabelWidget("UP")
        self.FilterUnknownLabel = LabelWidget("UNKNOWN")
        self.FilterBlockedLabel = LabelWidget("BLOCKED")

        self.FilterUpCheckbox = CheckboxInputWidget()
        self.FilterUnknownCheckbox = CheckboxInputWidget()
        self.FilterBlockedCheckbox = CheckboxInputWidget()

        self.FilterLayout = GLayoutWidget(v_spacing="sm")
        self.FilterLayout.addWidget(self.FilterUpLabel, 0, 0)
        self.FilterLayout.addWidget(self.FilterUnknownLabel, 0, 1)
        self.FilterLayout.addWidget(self.FilterBlockedLabel, 0, 2)
        self.FilterLayout.addWidget(self.FilterUpCheckbox, 1, 0)
        self.FilterLayout.addWidget(self.FilterUnknownCheckbox, 1, 1)
        self.FilterLayout.addWidget(self.FilterBlockedCheckbox, 1, 2)
        self.FilterLayout.addWidget(self.FilterError, 2, 0, 1, 4)

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
        self.Layout.addWidget(self.SelectNetworkTitle)
        self.Layout.addLayout(self.SelectNetworkLayout)
        self.Layout.addWidget(HLineWidget())
        self.Layout.addWidget(self.SelectPacketsTitle)
        self.Layout.addLayout(self.SelectPacketsLayout)
        self.Layout.addWidget(HLineWidget())
        self.Layout.addWidget(self.FilterTitle)
        self.Layout.addLayout(self.FilterLayout)
        self.Layout.addLayout(self.OutputLayout)
        self.Layout.addLayout(self.ButtonsLayout)

        # Setup
        self.setLayout(self.Layout)

    def get_filter_checkboxes(self):
        return [self.FilterUpCheckbox, self.FilterUnknownCheckbox, self.FilterBlockedCheckbox]
