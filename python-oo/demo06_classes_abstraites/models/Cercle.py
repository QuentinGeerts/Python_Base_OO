import math
from models.Forme import Forme

class Cercle(Forme):
    """Classe représentant un cercle."""

    def __init__(self, rayon):
        super().__init__()
        self.rayon = rayon
        self._nom = "Cercle"

    @property
    def nom(self):
        """Implémentation de l'attribut abstrait pour le nom du cercle."""
        return self._nom

    def aire(self):
        """Implémentation de la méthode aire pour un cercle."""
        import math
        return math.pi * self.rayon ** 2

    def perimetre(self):
        """Implémentation de la méthode périmètre pour un cercle."""
        import math
        return 2 * math.pi * self.rayon