from utils.formating import format_text, format_key_value


class WhoisLookupResult():

    def __init__(self):
        # Hoe benaming werkt: eerste woord zegt wat voor categorie het is
        # Bv: general: is algemen info, network: specifieke netwerk info

        self.general_asn = None

        self.general_asn_date = None

        self.general_asn_registery = None

        self.general_asn_cidr = None

        self.network_start_address = None

        self.network_end_address = None

        self.general_asn_country_code = None

        self.general_asn_description = None

        self.objects_contact = None



# hoe alle waarden vinden? --> met keys() aangezien dictionary is (zie test env)

    def build_search_result(self, result: dict):
        self.general_asn = result.get('asn')
        self.general_asn_date = result.get('asn_date')
        self.general_asn_registery = result.get('asn_registry')
        self.general_asn_cidr = result.get('asn_cidr')
        self.general_asn_country_code = result.get('asn_country_code')
        self.general_asn_description = result.get('asn_description')

        network = result.get('network')

        self.network_start_address = network.get('start_address')
        self.network_end_address = network.get('end_address')

        self.contact_builder(result)

    def contact_builder(self, result: dict):
        objects_dict = result.get('objects')
        first_key = list(objects_dict.keys())[0]

        first_dict = objects_dict.get(first_key)
        name = first_dict['contact']['name']
        address = first_dict['contact']['address']
        phone = first_dict['contact']['phone']
        email = first_dict['contact']['email']

        if first_dict['contact']['address']:
            addressTogether = first_dict['contact']['address'][0]["value"]
            address = addressTogether.replace("\n", ", ")

        if first_dict['contact']['phone']:
            phone = first_dict['contact']['phone'][0]["value"]

        if first_dict['contact']['email']:
            email = first_dict['contact']['email'][0]["value"]

        contact_list = {
            "name": name,
            "address": address,
            "phone": phone,
            "email": email
        }

        self.objects_contact = contact_list

    def to_text_extended(self):
        result = ""
        if self.general_asn:
            result += format_text("ASN:", sep='=')
            result += format_text(self.general_asn, nl=True)

        if self.general_asn_date:
            result += format_text("ASN allocation date:", sep="=")
            result += format_text(self.general_asn_date, nl=True)

        if self.general_asn_registery:
            result += format_text("Assigned ASN registry:", sep="=")
            result += format_text(self.general_asn_registery, nl=True)

        if self.general_asn_cidr:
            result += format_text("Assigned ASN CIDR range:", sep="=")
            result += format_text(self.general_asn_cidr, nl=True)

        if self.network_start_address:
            result += format_text("Network start address:", sep="=")
            result += format_text(self.network_start_address, nl=True)

        if self.network_end_address:
            result += format_text("Network end address:", sep="=")
            result += format_text(self.network_end_address, nl=True)

        if self.general_asn_country_code:
            result += format_text("Assigned ASN country code:", sep="=")
            result += format_text(self.general_asn_country_code, nl=True)

        if self.general_asn_description:
            result += format_text("ASN description:", sep="=")
            result += format_text(self.general_asn_description, nl=True)

        if self.objects_contact:
            result += format_text("Contact information:", sep="=")

            for key, value in self.objects_contact.items():
                if value:
                    result += format_key_value(key, value, list=True)

        return result
