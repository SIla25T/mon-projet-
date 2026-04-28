from abc import ABC, abstractmethod
from typing import List

class ElementNarratif(ABC):
    """Classe de base pour tous les éléments de l'ontologie."""
    def __init__(self, id_element: str, nom: str): 
        self.id_element = id_element
        self.nom = nom

    @abstractmethod
    def decrire(self) -> str:
        pass

class characters(ElementNarratif):
    """Classe représentant les personnages d'un conte."""
    def __init__(self, id_element: str, nom: str, role: str, traits: List[str]):
        super().__init__(id_element, nom)
        self.role = role
        self.traits = traits
    def decrire(self) -> str:
        return f"{self.nom} est un(e) {self.role}."
    
class location(ElementNarratif):
    """Représente un décor de l'histoire."""
    def __init__(self, id_element: str, nom: str):
        super().__init__(id_element, nom)
        
    def decrire(self) -> str:
        return f"Le lieu '{self.nom}' est un décor important de l'histoire."

        
    


