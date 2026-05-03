"""classe Characters"""
from dataclasses import dataclass
from classe_abstraite import ElementOntologie

@dataclass
class Characters (ElementOntologie):
    """classe pour les elememts personnage des fichiers json"""
    id: str
    name: str
    aliases: list
    role: str
    gender: str
    traits: list
    status: str
    def fusionner(self, data_text1, data_text2):
        """trouve les conflits"""
 # Implémentation du crossover pour fusionner les personnages
        personnages_fusionnes = []

        for perso_a in data_text1:
            personnages_fusionnes.append(perso_a)
        for perso_b in data_text2:
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
