from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QCheckBox, \
    QTextBrowser


class NslookupTab(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # domain input
        self.NsLabel = QLabel("Domain:")
        self.DomainEdit = QLineEdit()
        self.DomainEdit.setFixedWidth(200)
        self.DomainButton = QPushButton("Scan")

        self.Header = QHBoxLayout()
        self.Header.addWidget(self.NsLabel)
        self.Header.addSpacing(10)
        self.Header.addWidget(self.DomainEdit)
        self.Header.addSpacing(10)
        self.Header.addWidget(self.DomainButton)
        self.Header.addStretch(1)

        # possible options
        self.CheckboxNs = QCheckBox("NS")
        self.CheckboxA = QCheckBox("A")
        self.CheckboxAAAA = QCheckBox("AAAA")
        self.CheckboxMx = QCheckBox("MX")

        self.CheckBoxInput = QHBoxLayout()
        self.CheckBoxInput.addWidget(self.CheckboxNs)
        self.CheckBoxInput.addWidget(self.CheckboxA)
        self.CheckBoxInput.addWidget(self.CheckboxAAAA)
        self.CheckBoxInput.addWidget(self.CheckboxMx)

        # result of search
        self.Result = QTextBrowser()

        self.Resultoutput = QVBoxLayout()
        self.Resultoutput.addWidget(self.Result)

        # layout components
        self.Layout = QVBoxLayout()
        self.Layout.addLayout(self.Header)
        self.Layout.addSpacing(20)
        self.Layout.addLayout(self.CheckBoxInput)
        self.Layout.addSpacing(20)
        self.Layout.addLayout(self.Resultoutput)
        self.setLayout(self.Layout)
