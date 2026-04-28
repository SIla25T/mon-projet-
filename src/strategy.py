from abc import ABC, abstractmethod
from typing import List

from src.sous_classes.characters import Personnage

class FusionStrategy(ABC):
    """Classe de base pour les stratégies de fusion."""
    @abstractmethod
    def fusionner_personnage(self,liste_a: List[Personnage], liste_b: List[Personnage]) -> List[Personnage]:
        #methode pour fusioner les listes de personnages
        pass

class CrossoverStrategy(FusionStrategy):
    """Stratégie de fusion basée sur le crossover."""
    def fusionner_personnage(self, liste_a: List[Personnage], liste_b: List[Personnage]) -> List[Personnage]:
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
    
                    
                

