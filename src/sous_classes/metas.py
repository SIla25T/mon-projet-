from classe_abstraite import Conte

class Metas(Conte):
    def __init__(self,text, title, author, year, source, language, domain):
        self.text = text
        self.title = title
        self.author = author
        self.year = year
        self.source = source
        self.language = language
        self.domain = domain
    def conflit(self):
        """trouve les conflits"""