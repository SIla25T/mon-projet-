"""Classe Conte"""

from abc import ABC

class ElementOntologie(ABC):
    """Classe de base pour tous les éléments (ABC)."""
    def __init__(self):
        self.self = self

    # @classmethod
    # def fusionner(cls, data_text_1, data_text_2):
    #     """trouve les conflits et les résoud"""
    #     Implémentation du crossover pour fusionner les lieux
        # evenements_fusionnes = []
        # for evenement_a in data_text_1:
        #     evenements_fusionnes.append(evenement_a)
        # for evenement_b in data_text_2:
        #     conflit= False
        #     #changements_spéciaux()
        #     conflit= True
        #     break
        # if not conflit:
        #     evenements_fusionnes.append(evenement_b)
        # return evenements_fusionnes
