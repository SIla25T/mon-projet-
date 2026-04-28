<<<<<<< Updated upstream
"""Classe Relations"""
from dataclasses import dataclass
from src.classe_abstraite import Conte
#from input import data
from src.texts import data_text1, data_text2

@dataclass
class Relations (Conte):
    """classe pour les elememts relation des fichiers json"""
    text: int
    id: str
    subject : str
    predicate : str
    object : str
    type : str
    def conflit(self):
        """trouve les conflits"""

relations_text1 = [Relations(**relation) for relation in data_text1['relations']]
relations_text2 = [Relations(**relation) for relation in data_text2['relations']]
