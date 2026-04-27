"""Classe Conte"""

from abc import ABC, abstractmethod

class Conte(ABC):
    """Classe abstraite représentant toutes les constituantes d'un conte.
    toutes les sous-classes de Conte doivent avoir un id"""
    @abstractmethod
    def id(self):
        """retourne l'id de la constituante du conte"""
    def conflit(self):
        """retourne les conflits entre les contes"""