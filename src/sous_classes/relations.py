"""Classe Relations"""
from dataclasses import dataclass
from traitement_id import traiter_id_classe
from sous_classes.classe_abstraite import ElementOntologie

@dataclass
class Relations (ElementOntologie):
    """classe pour les elememts relation des fichiers json"""
    id: str
    subject : str # a comparer
    predicate : list
    object : str # a comparer
    type : list

    # def conflit(self):
    #     """trouve les conflits"""

    @classmethod
    def fusionner(cls, data_text_1, data_text_2):
        """trouve les conflits"""
        relations_fusionnes = list(data_text_1)

        for relation_b in data_text_2:
            conflit= False

            for relation_deja_range in relations_fusionnes:
            #     if relation_b.subject == relation_deja_range.subject and relation_b.object == relation_deja_range.object :
                if (set(relation_b.subject) & set(relation_deja_range.subject)) and \
                   (set(relation_b.object) & set(relation_deja_range.object)):
                    print(f"Fusion en cours : la relation entre {relation_b.subject} et {relation_b.object} est dans les deux histoires !")
                    #relation_deja_range.predicate.extend(relation_b.predicate)
                    #relation_deja_range.predicate = list(set(relation_deja_range.predicate))

                    #relation_deja_range.type.extend(relation_b.type)
                    #relation_deja_range.type = list(set(relation_deja_range.type))
                    relation_deja_range.id = traiter_id_classe(relation_deja_range.id)
                    relation_deja_range.predicate= list(set(relation_deja_range.predicate + relation_b.predicate))
                    relation_deja_range.type = list(set(relation_deja_range.type + relation_b.type))
                    conflit= True
                    break
            if not conflit:
                relations_fusionnes.append(relation_b)
        return relations_fusionnes
