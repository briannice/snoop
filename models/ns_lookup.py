from utils.formating import format_seconds_to_time, format_text, format_key_value


class NsLookupResult():

    def __init__(self):

        # [ns3.cloudflare.com. , ns4.cloudflare.com. , ...]
        self.NS = None

        # [104.16.132.229 , 104.16.133.229 , ...]
        self.A = None

        # [2606:4700::6810:85e5 , 2606:4700::6810:84e5 , ...]
        self.AAAA = None

        # [ mailstream-east.mxrecord.io. , mailstream-west.mxrecord.io. , ...]
        self.MX = None

        self.SOA = None

    def add_record(self, record_type: str, records):
        match record_type:
            case "NS":
                self.add_NS(records)
            case "A":
                self.add_A(records)
            case "AAAA":
                self.add_AAAA(records)
            case "MX":
                self.add_MX(records)
            case "SOA":
                self.add_SOA(records)

    def add_NS(self, records):
        if records is not None:
            self.NS = [str(r) for r in records]

    def add_A(self, records):
        if records is not None:
            self.A = [str(r) for r in records]

    def add_AAAA(self, records):
        if records is not None:
            self.AAAA = [str(r) for r in records]

    def add_MX(self, records):
        if records is not None:
            self.MX = [str(r.exchange) for r in records]

    def add_SOA(self, records):
        if records is not None:
            self.SOA = [
                {
                    "Primary name server": str(r.mname),
                    "Mail address": str(r.rname),
                    "Eefresh": format_seconds_to_time(r.refresh),
                    "Serial": str(r.serial),
                    "Retry": format_seconds_to_time(r.retry),
                    "Expire": format_seconds_to_time(r.expire),
                    "Default TTL": format_seconds_to_time(r.minimum),

                } for r in records
            ]

    def to_text_extended(self):
        result = ""
        if self.NS:
            result += self.format_NS()
        if self.A:
            result += self.format_A()
        if self.AAAA:
            result += self.format_AAAA()
        if self.MX:
            result += self.format_MX()
        if self.SOA:
            result += self.format_SOA()
        return result

    def format_NS(self):
        result = ""
        result += format_text("NS", sep="=")
        for record in self.NS:
            result += format_text(record, list=True)
        result += "\n"
        return result

    def format_A(self):
        result = ""
        result += format_text("A", sep="=")
        for record in self.A:
            result += format_text(record, list=True)
        result += "\n"
        return result

    def format_AAAA(self):
        result = ""
        result += format_text("AAAA", sep="=")
        for record in self.AAAA:
            result += format_text(record, list=True)
        result += "\n"
        return result

    def format_MX(self):
        result = ""
        result += format_text("MX", sep="=")
        for record in self.MX:
            result += format_text(record, list=True)
        result += "\n"
        return result

    def format_SOA(self):
        result = ""
        result += format_text("SOA", sep="=")
        for record in self.SOA:
            text = ""
            text += format_text(record["Primary name server"], sep="-")
            for key, value in record.items():
                if key == "Primary name server":
                    continue
                text += format_key_value(key, value, list=True)
            result += "\n"
            result += text
        result += "\n"
        return result
