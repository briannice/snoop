from typing import List

from widgets import ButtonWidget, HLineWidget, LabelWidget, TabWidget
from widgets.input import CheckboxInputWidget, TextInputWidget
from widgets.layout import GLayoutWidget, HLayoutWidget, VLayoutWidget


class NetworkScanningView(TabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Select network
        self.__SelectNetworkLabel = LabelWidget("Network")
        self.__SelectNetworkTextInput = TextInputWidget()

        self.__SelectNetworkLayout = HLayoutWidget()
        self.__SelectNetworkLayout.addWidget(self.__SelectNetworkLabel)
        self.__SelectNetworkLayout.addWidget(self.__SelectNetworkTextInput)

        # Select packets
        self.__SelectPacketsPingLabel = LabelWidget("Ping")
        self.__SelectPacketsSshLabel = LabelWidget("SSH")
        self.__SelectPacketsHttpLabel = LabelWidget("HTTP")
        self.__SelectPacketsHttpsLabel = LabelWidget("HTTPS")

        self.__SelectPacketsPingCheckbox = CheckboxInputWidget()
        self.__SelectPacketsSshCheckbox = CheckboxInputWidget()
        self.__SelectPacketsHttpCheckbox = CheckboxInputWidget()
        self.__SelectPacketsHttpsCheckbox = CheckboxInputWidget()

        self.__SelectPacketsLayout = GLayoutWidget()
        self.__SelectPacketsLayout.addWidget(self.__SelectPacketsPingLabel, 0, 0)
        self.__SelectPacketsLayout.addWidget(self.__SelectPacketsSshLabel, 0, 1)
        self.__SelectPacketsLayout.addWidget(self.__SelectPacketsHttpLabel, 0, 2)
        self.__SelectPacketsLayout.addWidget(self.__SelectPacketsHttpsLabel, 0, 3)

        self.__SelectPacketsLayout.addWidget(self.__SelectPacketsPingCheckbox, 1, 0)
        self.__SelectPacketsLayout.addWidget(self.__SelectPacketsSshCheckbox, 1, 1)
        self.__SelectPacketsLayout.addWidget(self.__SelectPacketsHttpCheckbox, 1, 2)
        self.__SelectPacketsLayout.addWidget(self.__SelectPacketsHttpsCheckbox, 1, 3)

        # Buttons
        self.__ButtonScan = ButtonWidget("Start scan")
        self.__ButtonClear = ButtonWidget("Clear output")

        self.__ButtonsLayout = HLayoutWidget()
        self.__ButtonsLayout.addWidget(self.__ButtonScan)
        self.__ButtonsLayout.addWidget(self.__ButtonClear)

        # Result
        self.__OutputLayout = VLayoutWidget()

        # Self
        self.__Layout = VLayoutWidget()
        self.__Layout.addLayout(self.__SelectNetworkLayout)
        self.__Layout.addWidget(HLineWidget())
        self.__Layout.addLayout(self.__SelectPacketsLayout)
        self.__Layout.addWidget(HLineWidget())
        self.__Layout.addLayout(self.__ButtonsLayout)
        self.__Layout.addLayout(self.__OutputLayout)

        # Setup
        self.setLayout(self.__Layout)

    def get_select_packets_checkboxes(self) -> List[CheckboxInputWidget]:
        return [
            self.__SelectPacketsPingCheckbox,
            self.__SelectPacketsSshCheckbox,
            self.__SelectPacketsHttpCheckbox,
            self.__SelectPacketsHttpsCheckbox,
        ]
