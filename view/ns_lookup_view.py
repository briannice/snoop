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
                self.handle_result_search_domain(lookupRecord(domain, rdataCheckbox), rdataCheckbox)

    def handle_result_search_domain(self, result: dns.rrset, typeData: dns.rdatatype):
        if result is not None:
            for re in result:
                if typeData == dns.rdatatype.MX:
                    # todo: add option to show preference value anyway if multiple mail servers?
                    self.Result.append(dns.rdatatype.to_text(typeData) + ": " + str(re.exchange))
                else:
                    self.Result.append(dns.rdatatype.to_text(typeData) + ": " + str(re))
        else:
            self.Result.append(dns.rdatatype.to_text(typeData) + ": " + "No records found")
