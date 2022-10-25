from lib.whois_search import whoisQuery
from ui import WhoisUi


class WhoisView(WhoisUi):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Handlers
        self.DomainButton.clicked.connect(self.handle_search_whois)

    def handle_search_whois(self):
        self.Result.clear()
        results = whoisQuery(self.DomainEdit.text())

        for result in results.keys():
            # todo: temp if to prevent overflow text, will get resolved when better outprint (look more into objects, good information)
            if result != "network" and result != "entities" and result != "objects":
                self.Result.append(result + ": " + str(results.get(result)))