"""classe Rules"""
from dataclasses import dataclass
from src.classe_abstraite import Conte
#from input import data
from src.texts import data_text1, data_text2

@dataclass
class Rules(Conte):
    """classe pour les elememts regles des fichiers json"""
    text : int
    id : str
    description : str
    affects : list # pas toujour
    event_concerned : list
    def conflit(self):
        """trouve les conflits"""

rules_text1 = [Rules(**rule) for rule in data_text1['rules']]
rules_text2 = [Rules(**rule) for rule in data_text2['rules']]
