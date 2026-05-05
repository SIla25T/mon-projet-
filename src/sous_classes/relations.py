"""Classe Relations"""
from dataclasses import dataclass
from sous_classes.classe_abstraite import ElementOntologie

@dataclass
class Relations (ElementOntologie):
    """classe pour les elememts relation des fichiers json"""
    id: str
    subject : str # a comparer
    predicate : str
    object : str # a comparer
    type : str
    def conflit(self):
        """trouve les conflits"""

    # fusionner :
            #       => si sujet et objet sont les memes => enrichire
            #       => predicates => liste ?
            #       => type => liste ?
    @classmethod
    def fusionner(cls, data_text_1, data_text_2):
        """trouve les conflits"""
        # Implémentation du crossover pour fusionner les relations
        relations_fusionnes = []
        for relation_a in data_text_1:
            relations_fusionnes.append(relation_a)
        for relation_b in data_text_2:
            conflit= False

            for relation_deja_range in relations_fusionnes:
                if relation_b.subject == relation_deja_range.subject and relation_b.object == relation_deja_range.object :
                    print(f"Fusion en cours : la relation entre {relation_b.subject} et {relation_b.object} est dans les deux histoires !")
                    #relation_deja_range.predicate.extend(relation_b.predicate)
                    #relation_deja_range.predicate = list(set(relation_deja_range.predicate))
                    #relation_deja_range.type.extend(relation_b.type)
                    #relation_deja_range.type = list(set(relation_deja_range.type))
                    conflit= True
                    break
            if not conflit:
                relations_fusionnes.append(relation_b)
        return relations_fusionnes
