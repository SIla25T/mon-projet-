"""classe Events"""
from dataclasses import dataclass
from traitement_id import traiter_id_classe
from .classe_abstraite import ElementOntologie

@dataclass
class Events (ElementOntologie):
    """classe pour les elememts evenement des fichiers json"""
    id: str
    name: str # a comparer
    order: int   # attemtion!!
    description: str
    participants: list
    location: str
    type: str
    trigger : str
    consequence: str
     # fusion events :
    #              => name = ce qui justifie la fusion
    #              => order => incrémenter / deux ordres paralleles ?
    #              => description => transformer en liste ?/faire une string plus
    #                   longue/en eliminer un ?
    #              => participants => ajouter les personnages (personnages ont plus les memes id!!)
    #              => location ? => ajouter les lieux (ont plus les memes id !!!)
    #              => type => ?
    #              => trigger => attention incrémentation d'id
    #              => consequences => attention incrémentation d'id
    @classmethod
    def fusionner(cls, data_text_1, data_text_2):
        """trouve les conflits et les résoud"""
        # Implémentation du crossover pour fusionner les lieux
        evenements_fusionnes = []
        for evenement_a in data_text_1:
            evenements_fusionnes.append(evenement_a)
        for evenement_b in data_text_2:
            conflit= False

            for evenement_deja_range in evenements_fusionnes:
                if evenement_b.name == evenement_deja_range.name:
                    print(f"Fusion en cours : {evenement_b.name} est dans les deux histoires !")
                    evenement_deja_range.participants.extend(evenement_b.participants)
                    evenement_deja_range.participants = list(set(evenement_deja_range.participants))
                    evenement_deja_range.id = traiter_id_classe(evenement_deja_range.id)
                    conflit= True
                    break
            if not conflit:
                evenements_fusionnes.append(evenement_b)
        return evenements_fusionnes
