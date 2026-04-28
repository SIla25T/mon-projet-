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
    def fusionner(self):
        """trouve les conflits"""
 # Implémentation du crossover pour fusionner les personnages
        personnages_fusionnes = []

        for perso_a in liste_a: 
            personnages_fusionnes.append(perso_a)
        for perso_b in liste_b:
            conflit= False 

            for perso_deja_range in personnages_fusionnes:
                if perso_b.nom== perso_deja_range.nom:
                    print(f"Fusion en cours : {perso_b.nom} est dans les deux histoires !")
                    perso_deja_range.traits.extend(perso_b.traits)
                    perso_deja_range.traits = list(set(perso_deja_range.traits))
                    conflit= True 
                    break
            if not conflit:
                personnages_fusionnes.append(perso_b)
        return personnages_fusionnes



characters_text1 = [Characters(**character) for character in data_text1['characters']]
characters_text2 = [Characters(**character) for character in data_text2['characters']]
characters_text1.fusionner(characters_text2)



print(characters_text1) 
print(characters_text2.id)
