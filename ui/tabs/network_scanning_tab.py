from ipaddress import IPv4Network
from typing import List

from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout,
    QTextBrowser
)

from lib.scanning.icmp import PingScanResult
from workers.network_scanning_worker import NetworkScanningWorker


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

        # Handlers
        self.NetworkScanButton.clicked.connect(self.handle_scan_start)

    def handle_scan_start(self):
        network = self.NetworkLineEdit.text()
        worker = NetworkScanningWorker(IPv4Network(network))
        worker.signals.finished.connect(self.handle_scan_finished)
        worker.signals.progress.connect(self.handle_scan_progress)
        worker.signals.result.connect(self.handle_scan_result)

        QThreadPool.globalInstance().start(worker)

    def handle_scan_progress(self, progress: int):
        print(f"Progress: {progress}")

    def handle_scan_finished(self, finished: bool):
        print(f"Finished: {finished}")

    def handle_scan_result(self, result: List[PingScanResult]):
        for r in result:
            self.Output.append(r.__str__())
