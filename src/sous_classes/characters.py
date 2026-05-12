"""classe Characters"""
from dataclasses import dataclass
from traitement_id import traiter_id_classe, traiter_id_text
from .classe_abstraite import ElementOntologie

@dataclass
class Characters (ElementOntologie):
    """classe pour les elememts personnage des fichiers json"""
    id: str
    name: str
    aliases: list
    role: list
    gender: list
    traits: list
    status: list
<<<<<<< Updated upstream

    @classmethod
    def fusionner(cls, data_text_1, data_text_2, text1, text2):
        """trouve les conflits"""
    # Implémentation du crossover pour fusionner les personnages
        personnages_fusionnes = []
        for perso_a in data_text_1:
            personnages_fusionnes.append(perso_a)
        for perso_b in data_text_2:
            conflit= False
=======
   
    @classmethod
    def fusionner(cls, data_text_1, data_text_2):
        """Trouve les conflits et fusionne les personnages si un nom correspond"""
        personnages_fusionnes = list(data_text_1)
>>>>>>> Stashed changes

        for perso_b in data_text_2:
            conflit = False
            
            for perso_deja_range in personnages_fusionnes:
                if perso_b.name == perso_deja_range.name:
                    print(f"Fusion en cours : {perso_b.name} est dans les deux histoires !")
<<<<<<< Updated upstream
                    perso_deja_range.aliases.extend(perso_b.aliases)
                    perso_deja_range.aliases = list(set(perso_deja_range.aliases))

                    perso_deja_range.traits.extend(perso_b.traits)
                    perso_deja_range.traits = list(set(perso_deja_range.traits))
                    # changement id text1
                    perso_deja_range.id = traiter_id_classe(perso_deja_range.id)
                    text1_id_char = traiter_id_text(text1, perso_deja_range.id)
                    text2_id_char = traiter_id_text(text2, perso_b.id)
                    conflit= True
                    break
            if not conflit:
                personnages_fusionnes.append(perso_b)
        return personnages_fusionnes, text1_id_char, text2_id_char
=======
                    perso_deja_range.aliases = list(set(perso_deja_range.aliases + perso_b.aliases))
                    perso_deja_range.role = list(set(perso_deja_range.role + perso_b.role))
                    perso_deja_range.gender = list(set(perso_deja_range.gender + perso_b.gender))
                    perso_deja_range.traits = list(set(perso_deja_range.traits + perso_b.traits))
                    perso_deja_range.status = list(set(perso_deja_range.status + perso_b.status))
                    conflit = True
                    break
                if not conflit: 
                    personnages_fusionnes.append(perso_b)
                return personnages_fusionnes
            


#     def fusionner(cls, data_text_1, data_text_2):
#         """trouve les conflits"""
#  # Implémentation du crossover pour fusionner les personnages
#         personnages_fusionnes = []
#         for perso_a in data_text_1:
#             personnages_fusionnes.append(perso_a)
#         for perso_b in data_text_2:
#             conflit= False

#             for perso_deja_range in personnages_fusionnes:
#                 if perso_b.name == perso_deja_range.name:
#                     print(f"Fusion en cours : {perso_b.name} est dans les deux histoires !")
#                     perso_deja_range.aliases.extend(perso_b.aliases)
#                     perso_deja_range.aliases = list(set(perso_deja_range.aliases))
#                     perso_deja_range.traits.extend(perso_b.traits)
#                     perso_deja_range.traits = list(set(perso_deja_range.traits))
#                     perso_deja_range.role.extend(perso_b.role) 
#                     perso_deja_range.role = list(set(perso_deja_range.role))
#                     perso_deja_range.status.extend(perso_b.status)
#                     perso_deja_range.status = list(set(perso_deja_range.status))
#                     conflit= True
#                     break
#             if not conflit:
#                 personnages_fusionnes.append(perso_b)
#         # modification des id dans text1 et text2
>>>>>>> Stashed changes
