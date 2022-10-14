from ui import NslookupUi
import dns.rrset, dns.rdatatype
from lib.domainresearch import lookupRecord


class NslookpView(NslookupUi):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Handlers
        self.DomainButton.clicked.connect(self.handle_search_domain)

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
                    self._sub_search(lookupRecord(str(re.exchange), dns.rdatatype.A))
                    self._sub_search(lookupRecord(str(re.exchange), dns.rdatatype.AAAA))
                else:
                    self.Result.append(dns.rdatatype.to_text(typeData) + ": " + str(re))

                    # Same as with MX, but on top of it for NS
                    if typeData == dns.rdatatype.NS:
                        self._sub_search(lookupRecord(str(re), dns.rdatatype.A))
                        self._sub_search(lookupRecord(str(re), dns.rdatatype.AAAA))
        else:
            self.Result.append(dns.rdatatype.to_text(typeData) + ": " + "No records found")

    def _sub_search(self, result: dns.rrset):
        if result is not None:
            for re in result:
                self.Result.append("\t" + dns.rdatatype.to_text(re.rdtype) + ": " + str(re))
