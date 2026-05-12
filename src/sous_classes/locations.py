
"""Classe Locations"""
from dataclasses import dataclass, field
from traitement_id import traiter_id_classe, traiter_id_text
from .classe_abstraite import ElementOntologie

@dataclass
class Locations(ElementOntologie):
    """classe pour les elememts localisation des fichiers json"""
    id: str
    name: str
    type: list
    description: list
    atmosphere: list
    parent_location: str = field(default = None)

    # fusion lieux :
    #              => nom = ce qui justifie la fusion
    #              => type ? => transformer en liste ?/faire une string plus longue/en eliminer un ?
    #              => description ? => test
    #              => athmosphère ?
    #              => parent_location ?
    @classmethod
    def fusionner(cls, data_text_1, data_text_2, text1, text2):
        """trouve les conflits"""

        lieux_fusionnes= list(data_text_1)

        for lieu_b in data_text_2:
            conflit= False

        # lieux_fusionnes = []
        # for lieu_a in data_text_1:
        #     lieux_fusionnes.append(lieu_a)
        # for lieu_b in data_text_2:
        #     conflit= False

            for lieu_deja_range in lieux_fusionnes:
                if lieu_b.name == lieu_deja_range.name:
                    print(f"Fusion en cours : {lieu_b.name} est dans les deux histoires !")
                    lieu_deja_range.type = list(set(lieu_deja_range.type + lieu_b.type))
                    lieu_deja_range.description = list(set(lieu_deja_range.description + lieu_b.description))
                    lieu_deja_range.atmosphere = list(set(lieu_deja_range.atmosphere + lieu_b.atmosphere))
                    conflit= True
                    # changement id text1
                    lieu_deja_range.id = traiter_id_classe(lieu_deja_range.id)
                    text1_id_lieu = traiter_id_text(text1, lieu_deja_range.id)
                    text2_id_lieu = traiter_id_text(text2, lieu_b.id)
                    break
            if not conflit:
                lieux_fusionnes.append(lieu_b)
        return lieux_fusionnes, text1_id_lieu, text2_id_lieu
