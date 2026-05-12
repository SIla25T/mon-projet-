"""classe Rules"""
from dataclasses import dataclass, field
from traitement_id import traiter_id_classe
from sous_classes.classe_abstraite import ElementOntologie

@dataclass
class Rules(ElementOntologie):
    """classe pour les elememts regles des fichiers json"""
    id : str
    description : str # a comparer
    type : list
    affects : list = field(default_factory=list) # pas toujours
    events_concerned : list = field(default_factory=list)
    # fusionner :
        #       => descriptions = à comparer
        #       => type = a ajouter ?
        #       => fusionner les affects
        #       => fusionner les elements concernés
    @classmethod
    def fusionner(cls, data_text_1, data_text_2):
        """trouve les conflits"""
    # Implémentation du crossover pour fusionner les personnages
        regles_fusionnes = list(data_text_1)
        # for regle_a in data_text_1:
        #     regles_fusionnes.append(regle_a)
        for regle_b in data_text_2:
            conflit= False

            for regle_deja_range in regles_fusionnes:
<<<<<<< Updated upstream
                if regle_b.description == regle_deja_range.description:
                    print(f"Fusion en cours : {regle_b.description} est dans les deux histoires !")
                    regle_deja_range.affects.extend(regle_b.affects)
                    regle_deja_range.affects = list(set(regle_deja_range.affects))
                    regle_deja_range.events_concerned.extend(regle_b.events_concerned)
                    regle_deja_range.events_concerned = list(set(regle_deja_range.events_concerned))
                    regle_deja_range.id = traiter_id_classe(regle_deja_range.id)
=======
                if set(regle_b.description) & set(regle_deja_range.description):
                    print(f"Fusion en cours : correspondance trouvée pour la règle {regle_b.description} !")
                    regle_deja_range.type = list(set(regle_deja_range.type + regle_b.type))
                    regle_deja_range.affects = list(set(regle_deja_range.affects + regle_b.affects))
                    regle_deja_range.events_concerned = list(set(regle_deja_range.events_concerned + regle_b.events_concerned))
>>>>>>> Stashed changes
                    conflit= True
                    break
            if not conflit:
                regles_fusionnes.append(regle_b)
        return regles_fusionnes
