from widgets import ButtonWidget, GroupWidget, LabelWidget, TabWidget, TextWidget
from widgets.input import CheckboxInputWidget, TextInputWidget
from widgets.layout import GLayoutWidget, HLayoutWidget, VLayoutWidget


class NetworkScanningUi(TabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Title
        self.Title = LabelWidget("Network scanning", type="title")

        # Select network
        self.SelectNetworkLabel = LabelWidget("Host", type="label")
        self.SelectNetworkTextInput = TextInputWidget()
        self.SelectNetworkError = LabelWidget("", type="error")
        self.SelectNetworkInfo = LabelWidget("Example: 192.168.56.1", type="help")

        self.SelectNetworkLayout = GLayoutWidget(h_spacing="sm", v_spacing="sm")
        self.SelectNetworkLayout.addWidget(self.SelectNetworkLabel, 0, 0, 1, 1)
        self.SelectNetworkLayout.addWidget(self.SelectNetworkTextInput, 0, 1, 1, 1)
        self.SelectNetworkLayout.addWidget(self.SelectNetworkInfo, 0, 2, 1, 1)

        # Select packets
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

        self.SelectPacketsGroup = GroupWidget("Select protocols", self.SelectPacketsLayout)

        # Filter
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

        self.FilterGroup = GroupWidget("Filter results", self.FilterLayout)

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
        self.Layout.addWidget(self.Title)
        self.Layout.addLayout(self.SelectNetworkLayout)
        self.Layout.addWidget(self.SelectPacketsGroup)
        self.Layout.addWidget(self.FilterGroup)
        self.Layout.addLayout(self.OutputLayout)
        self.Layout.addLayout(self.ButtonsLayout)

        # Setup
        self.setLayout(self.Layout)

    def get_packet_checkboxes(self):
        return [
            self.SelectPacketsPingCheckbox,
            self.SelectPacketsSshCheckbox,
            self.SelectPacketsHttpCheckbox,
            self.SelectPacketsHttpsCheckbox
        ]

    def get_filter_checkboxes(self):
        return [
            self.FilterUpCheckbox,
            self.FilterUnknownCheckbox,
            self.FilterBlockedCheckbox
        ]
