from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QCheckBox, \
    QTextBrowser
import dns.rrset, dns.rdatatype
from lib.domainresearch.nslookup import lookupRecord


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

        self.Checkboxes = [QCheckBox("NS"), QCheckBox("A"), QCheckBox("AAAA"), QCheckBox("MX"), QCheckBox("SOA")]

        self.CheckBoxInput = QHBoxLayout()

        for x in range(len(self.Checkboxes)):
            self.CheckBoxInput.addWidget(self.Checkboxes[x])

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

        # event handlers
        self.DomainButton.clicked.connect(self.handle_search_domain)

    def handle_search_domain(self):
        domain = self.DomainEdit.text()
        self.Result.clear()

        for checkbox in range(len(self.Checkboxes)):
            if self.Checkboxes[checkbox].checkState() == Qt.Checked:
                rdataCheckbox = dns.rdatatype.from_text(self.Checkboxes[checkbox].text())
                self.handle_result_search_domain(lookupRecord(domain, rdataCheckbox), rdataCheckbox)

    def handle_result_search_domain(self, result: dns.rrset, searchType: dns.rdatatype.RdataType):
        if result is not None:
            for re in result:
                typeData = dns.rdatatype.to_text(searchType)
                if re.rdtype == dns.rdatatype.MX:
                    self.Result.append(typeData + ": " + str(re.exchange))
                else:
                    self.Result.append(typeData + ": " + str(re))
        else:
            typeData = dns.rdatatype.to_text(searchType)
            self.Result.append(typeData + ": " + "No records found")
