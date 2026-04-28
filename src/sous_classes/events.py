<<<<<<< Updated upstream
"""classe Events"""
from dataclasses import dataclass
from src.classe_abstraite import Conte
#from input import data => pour  quand ca sera relier à input
from src.texts import data_text1, data_text2

@dataclass
class Events (Conte):
    """classe pour les elememts evenement des fichiers json"""
    text: int
    id: str
    name: str
    order: int
    description: str
    participants: list
    location: str
    type: str
    trigger : str
    consequences: str
    def conflit(self):
        """trouve les conflits"""

events_text1 = [Events(**event) for event in data_text1['events']]
events_text2 = [Events(**event) for event in data_text2['events']]