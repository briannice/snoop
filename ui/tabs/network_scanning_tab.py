from PyQt5.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout,
    QTextBrowser
)


class NetworkScanningTab(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Header
        self.NetworkLabel = QLabel("Network:")
        self.NetworkLineEdit = QLineEdit()
        self.NetworkLineEdit.setFixedWidth(200)
        self.NetworkScanButton = QPushButton("Scan")

        self.Header = QHBoxLayout()
        self.Header.addWidget(self.NetworkLabel)
        self.Header.addSpacing(10)
        self.Header.addWidget(self.NetworkLineEdit)
        self.Header.addSpacing(10)
        self.Header.addWidget(self.NetworkScanButton)
        self.Header.addStretch(1)

        # Content
        self.Output = QTextBrowser()

        self.Content = QVBoxLayout()
        self.Content.addWidget(self.Output)

        # Layout
        self.Layout = QVBoxLayout()
        self.Layout.addLayout(self.Header)
        self.Layout.addSpacing(20)
        self.Layout.addLayout(self.Content)
        self.setLayout(self.Layout)

        #
        self.setContentsMargins(20, 20, 20, 20)
