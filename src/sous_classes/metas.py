"""classe Metas"""
from dataclasses import dataclass
from .classe_abstraite import ElementOntologie

@dataclass
class Metas(ElementOntologie):
    """classe pour les metas données des fichiers json"""
    title: str
    author: str
    year: int
    source: str
    language: str
    domain: str

    @classmethod
    def fusionner(cls, data_text_1, data_text_2):
        """trouve les conflits et les résoud"""
        # Implémentation du crossover pour fusionner les lieux
        evenements_fusionnes = []
        for evenement_a in data_text_1:
            evenements_fusionnes.append(evenement_a)
        for evenement_b in data_text_2:
            conflit= False

            for evenement_deja_range in evenements_fusionnes:
                if evenement_b == evenement_deja_range :
                    print(f"Fusion en cours : {evenement_b.name} est dans les deux histoires !")
                    conflit= True
                    break
            if not conflit:
                evenements_fusionnes.append(evenement_b)
        return evenements_fusionnes
