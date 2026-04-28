"""classe Characters"""
from dataclasses import dataclass
from classe_abstraite import Conte
#from input import data
from input import data_text1, data_text2

@dataclass
class Characters (Conte):
    """classe pour les elememts personnage des fichiers json"""
    id: str
    name: str
    aliases: list
    role: str
    gender: str
    traits: list
    status: str
    def conflit(self):
        """trouve les conflits"""

characters_text1 = [Characters(**character) for character in data_text1['characters']]
characters_text2 = [Characters(**character) for character in data_text2['characters']]

print(characters_text1)
