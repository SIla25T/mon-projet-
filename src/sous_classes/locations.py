<<<<<<< Updated upstream
"""Classe Locations"""
from dataclasses import dataclass
from classe_abstraite import Conte
#from input import data
from input import data_text1, data_text2

@dataclass
class Locations(Conte):
    """classe pour les elememts localisation des fichiers json"""
    id: str
    name: str
    type: str
    description: str
    atmosphere: str
    parent_location: str # pas toujours
    # fusion lieux => incrémentation des id 
    #              => nom = ce qui justifie la fusion
    #              => type ? => transformer en liste ? / faire une string plus longue / en eliminer un ?
    #              => description ? => test 
    #              => athmosphère ?
    #              => parent_location ?
    def fusionner(cls, data_text_1, data_text_2):
        """trouve les conflits"""
    # Implémentation du crossover pour fusionner les lieux
        lieux_fusionnes = []
        i=1
        for lieu_a in data_text_1:
            lieux_fusionnes.append(lieu_a)
        for lieu_b in data_text_2:
            conflit= False
      
            for lieu_deja_range in lieux_fusionnes:
                if lieu_b.name == lieu_deja_range.name:
                    print(f"Fusion en cours : {lieu_b.name} est dans les deux histoires !")
                    if i<10 :
                        lieu_deja_range.id = f"char_0{i}"
                    elif i>=10 :
                        lieu_deja_range.id = f"char_{i}"
                    lieu_deja_range.description.extend(lieu_b.description)
                    lieu_deja_range.description = list(set(lieu_deja_range.description))
                    conflit= True
                    i=i+1
                    break
            if not conflit:
                lieux_fusionnes.append(lieu_b)
        return lieux_fusionnes

