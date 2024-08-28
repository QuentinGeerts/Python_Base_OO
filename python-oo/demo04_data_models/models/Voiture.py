class Voiture:
    """Classe représentant une voiture."""

    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.__annee = 2024

    def __repr__(self):
        return f"Voiture(marque='{self.marque}', modele='{self.modele}')"

    def __str__(self):
        return f"{self.marque} {self.modele}"

    def __getattr__(self, attr):
        if attr == "annee":
            return self.__annee

    def __setattr__(self, attr, valeur):
        if attr == "annee":
            if isinstance(valeur, int) and 1900 <= valeur <= 2024:
                self.__dict__[attr] = valeur
            else:
                raise ValueError("Année invalide.")
        else:
            super().__setattr__(attr, valeur)

    def __delattr__(self, attr):
        if attr == "annee":
            raise AttributeError("Année ne peut pas être supprimée.")
        else:
            super().__delattr__(attr)

