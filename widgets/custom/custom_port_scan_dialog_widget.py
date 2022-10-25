from models.results import PortScanConclusion
from widgets.base import BaseDialogWidget, BaseLabelWidget, BaseListWidget, BaseVBoxLayoutWidget


class CustomPortScanDialogWidget(BaseDialogWidget):

    def __init__(self, port_scan_conclusion: PortScanConclusion):
        super().__init__()

        port = port_scan_conclusion.port
        state = port_scan_conclusion.state
        results = port_scan_conclusion.results

        # Helpers
        title = f"Port {port}: {state}"

        # Widgets
        self.col = BaseVBoxLayoutWidget()
        self.title = BaseLabelWidget(type="title", text=title)
        self.list = BaseListWidget()

        # Layout
        self.col.addWidget(self.title)
        self.col.addWidget(self.list)
        self.setLayout(self.col)

        # Styling
        for r in results:
            self.list.addItem(r.to_text_extended())
        self.setWindowTitle(title)
