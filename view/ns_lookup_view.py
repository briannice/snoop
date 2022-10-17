from ui import NslookupUi
import dns.rrset, dns.rdatatype
from lib.domainresearch import lookupRecord


class NslookpView(NslookupUi):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Handlers
        self.CheckAllButton.clicked.connect(self.handle_check_all_checkboxes)
        self.UncheckAllButton.clicked.connect(self.handle_uncheck_all_checkboxes)
        self.DomainButton.clicked.connect(self.handle_search_domain)

    def handle_check_all_checkboxes(self):
        for checkbox in range(len(self.Checkboxes)):
            self.Checkboxes[checkbox].setChecked(True)

    def handle_uncheck_all_checkboxes(self):
        for checkbox in range(len(self.Checkboxes)):
            self.Checkboxes[checkbox].setChecked(False)

    def handle_search_domain(self):
        domain = self.DomainEdit.text()
        self.Result.clear()

        for checkbox in range(len(self.Checkboxes)):
            if self.Checkboxes[checkbox].isChecked():
                rdataCheckbox = dns.rdatatype.from_text(self.Checkboxes[checkbox].text())
                self._handle_result_search_domain(lookupRecord(domain, rdataCheckbox), rdataCheckbox)

    def _handle_result_search_domain(self, result: dns.rrset, typeData: dns.rdatatype):
        if result is not None:
            for re in result:
                if typeData == dns.rdatatype.MX:
                    # todo: add option to show preference value anyway if multiple mail servers?
                    self.Result.append(dns.rdatatype.to_text(typeData) + ": " + str(re.exchange))

                    # Search on IP adresses related to MX
                    self._sub_search(str(re.exchange))
                else:
                    self.Result.append(dns.rdatatype.to_text(typeData) + ": " + str(re))

                    # Same as with MX, but on top of it for NS
                    if typeData == dns.rdatatype.NS:
                        self._sub_search(str(re))
        else:
            self.Result.append(dns.rdatatype.to_text(typeData) + ": " + "No records found")

    def _sub_search(self, domain: str):
        dnsTypes = [dns.rdatatype.A, dns.rdatatype.AAAA]

        for dnsType in range(len(dnsTypes)):
            q = lookupRecord(domain, dnsTypes[dnsType])
            if q is not None:
                for result in q:
                    self.Result.append("\t" + dns.rdatatype.to_text(result.rdtype) + ": " + str(result))
