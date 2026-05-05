"""classe Rules"""
from dataclasses import dataclass, field
from sous_classes.classe_abstraite import ElementOntologie

@dataclass
class Rules(ElementOntologie):
    """classe pour les elememts regles des fichiers json"""
    id : str
    description : str # a comparer
    affects : list = field(default = None) # pas toujour
    event_concerned : list
    # fusionner => mettre un conteur pour incrementer l'id ^
        #       => descriptions = à comparer
        #       => fusionner les affects
        #       => fusionner les elements concernés
    @classmethod
    def fusionner(cls, data_text_1, data_text_2):
        """trouve les conflits"""
    # Implémentation du crossover pour fusionner les personnages
        regles_fusionnes = []
        i=1
        for regle_a in data_text_1:
            regles_fusionnes.append(regle_a)
        for regle_b in data_text_2:
            conflit= False

            for regle_deja_range in regles_fusionnes:
                if regle_b.description == regle_deja_range.description:
                    print(f"Fusion en cours : {regle_b.description} est dans les deux histoires !")
                    if i<10 :
                        regle_deja_range.id = f"char_0{i}"
                    elif i>=10 :
                        regle_deja_range.id = f"char_{i}"
                    regle_deja_range.affects.extend(regle_b.affects)
                    regle_deja_range.affects = list(set(regle_deja_range.affects))
                    regle_deja_range.event_concerned.extend(regle_b.event_concerned)
                    regle_deja_range.event_concerned = list(set(regle_deja_range.event_concerned))
                    conflit= True
                    i=i+1
                    break
            if not conflit:
                regles_fusionnes.append(regle_b)
        return regles_fusionnes
