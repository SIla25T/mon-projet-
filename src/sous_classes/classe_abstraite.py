"""Classe Conte"""

from abc import ABC, abstractmethod

class ElementOntologie(ABC):
    """Classe de base pour tous les éléments (ABC)."""
    def __init__(self, id_entree: str, nom: str):
        self.id_entree = id_entree
        self.nom = nom

    @abstractmethod
    def fusionner(self):
        """retourne les conflits entre les contes"""
    