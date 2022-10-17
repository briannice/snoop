from datetime import timedelta

import dns.rdatatype
import dns.rrset

from lib.domainresearch import lookupRecord
from ui import NslookupUi


def _seconds_to_readable_format(sec: int):
    td_str = str(timedelta(seconds=sec))
    x = td_str.split(':')
    return x[0] + ' Hours ' + x[1] + ' Minutes ' + x[2] + ' Seconds'


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
                elif typeData == dns.rdatatype.SOA:
                    self.Result.append(dns.rdatatype.to_text(typeData) + ": ")
                    self._format_soa_record(re)
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

    def _format_soa_record(self, soa: dns.rdatatype.SOA):
        self.Result.append("  primary name server: " + str(soa.mname))
        self.Result.append("  responsible name server: " + str(soa.rname))
        self.Result.append("  serial: " + str(soa.serial))  # moet zo blijven want is geen tijd
        self.Result.append("  refresh: " + _seconds_to_readable_format(soa.refresh))
        self.Result.append("  retry: " + _seconds_to_readable_format(soa.retry))
        self.Result.append("  expire: " + _seconds_to_readable_format(soa.expire))
        self.Result.append("  default TTL: " + _seconds_to_readable_format(soa.minimum))
