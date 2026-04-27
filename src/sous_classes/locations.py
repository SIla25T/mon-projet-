"""Classe Locations"""
from dataclasses import dataclass
from classe_abstraite import Conte
#from input import data
from texts import data_text1, data_text2

@dataclass
class Locations(Conte):
    """classe pour les elememts localisation des fichiers json"""
    text: int
    id: str
    name: str
    type: str
    description: str
    atmosphere: str
    parent_location: str # pas toujours
    def conflit(self):
        """trouve les conflits"""

locations_text1 = [Locations(**location) for location in data_text1['locations']]
locations_text2 = [Locations(**location) for location in data_text2['locations']]