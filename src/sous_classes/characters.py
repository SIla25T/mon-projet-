"""classe Characters"""
from dataclasses import dataclass
from .classe_abstraite import ElementOntologie

@dataclass
class Characters (ElementOntologie):
    """classe pour les elememts personnage des fichiers json"""
    id: str
    name: str
    aliases: list
    role: list
    gender: str
    traits: list
    status: list
    # fusionner => mettre un conteur pour incrementer l'id ^
        #       => fusionner les roles ?
        #       => fusionner les aliases ^
        #       => fusionner les traits  ^
        #       => que faire si genre sont differents ?
        #       => fusionner le statut ?
    @classmethod
    def fusionner(cls, data_text_1, data_text_2):
        """trouve les conflits"""
 # Implémentation du crossover pour fusionner les personnages
        personnages_fusionnes = []
        i=1
        for perso_a in data_text_1:
            personnages_fusionnes.append(perso_a)
        for perso_b in data_text_2:
            conflit= False

            for perso_deja_range in personnages_fusionnes:
                if perso_b.name == perso_deja_range.name:
                    print(f"Fusion en cours : {perso_b.name} est dans les deux histoires !")
                    if i<10 :
                        perso_deja_range.id = f"char_0{i}"
                    elif i>=10 :
                        perso_deja_range.id = f"char_{i}"
                    perso_deja_range.aliases.extend(perso_b.aliases)
                    perso_deja_range.aliases = list(set(perso_deja_range.aliases))
                    perso_deja_range.traits.extend(perso_b.traits)
                    perso_deja_range.traits = list(set(perso_deja_range.traits))
                    conflit= True
                    i=i+1
                    break
            if not conflit:
                personnages_fusionnes.append(perso_b)
        # modification des id dans text1 et text2

        return personnages_fusionnes
