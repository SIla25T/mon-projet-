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
