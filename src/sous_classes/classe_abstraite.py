"""Classe Conte"""

from abc import ABC, abstractmethod

class ElementOntologie(ABC):
    """Classe de base pour tous les éléments (ABC)."""
    def __init__(self):
        self.self = self


    @classmethod
    def fusionner(cls, data_text_1, data_text_2):
        """retourne les conflits entre les contes"""
