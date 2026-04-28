<<<<<<< Updated upstream
"""classe Metas"""
from dataclasses import dataclass
from classe_abstraite import Conte
#from input import data
from texts import data_text1, data_text2

@dataclass
class Metas(Conte):
    """classe pour les metas données des fichiers json"""
    text: int
    title: str
    author: str
    year: int
    source: str
    language: str
    domain: str
    def conflit(self):
        """trouve les conflits"""

metas_text1 = [Metas(**meta) for meta in data_text1['metas']]
metas_text2 = [Metas(**meta) for meta in data_text2['metas']]


# from src.classe_abstraite import ElementOntologie

# class Metas(ElementOntologie):
#     def __init__(self, text: str, title: str, author: str, year: str, source: str, language: str, domain: str):
#         super().__init__(id_entrée="meta_info", nom="title")

#         self.text = text
#         self.title = title
#         self.author = author
#         self.year = year
#         self.source = source
#         self.language = language
#         self.domain = domain
    
