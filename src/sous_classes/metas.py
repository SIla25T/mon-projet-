from classe_abstraite import Conte

class Metas(Conte):
    def __init__(self, title, author, year, source, language, domain):
        self.title = title
        self.author = author
        self.year = year
        self.source = source
        self.language = language
        self.domain = domain

        
    def id(self):
        return #id...