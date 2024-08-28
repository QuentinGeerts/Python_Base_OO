from models.Forme import Forme

class Rectangle(Forme):
    """Classe représentant un rectangle."""

    def __init__(self, largeur, hauteur):
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur
        self._nom = "Rectangle"

    @property
    def nom(self):
        """Implémentation de l'attribut abstrait pour le nom du rectangle."""
        return self._nom

    def aire(self):
        """Implémentation de la méthode aire pour un rectangle."""
        return self.largeur * self.hauteur

    def perimetre(self):
        """Implémentation de la méthode périmètre pour un rectangle."""
        return 2 * (self.largeur + self.hauteur)