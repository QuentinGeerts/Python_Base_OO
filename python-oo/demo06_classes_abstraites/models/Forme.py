from abc import ABC, abstractmethod


class Forme(ABC):
    """Classe abstraite représentant une forme géométrique."""

    def __init__(self):
        # Définir des attributs abstraits à initialiser dans les classes dérivées
        self._nom = None

    @property
    @abstractmethod
    def nom(self):
        """Attribut abstrait pour le nom de la forme."""
        pass

    @abstractmethod
    def aire(self):
        """Méthode abstraite pour calculer l'aire de la forme."""
        pass

    @abstractmethod
    def perimetre(self):
        """Méthode abstraite pour calculer le périmètre de la forme."""
        pass

    def __str__(self):
        return f"{self.nom}: aire={self.aire()}, périmètre={self.perimetre()}"
