class Livre:
    """Classe représentant un livre avec des membres statiques pour la gestion des livres."""

    # Attribut statique pour suivre le nombre total de livres
    nombre_livres = 0

    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        # Incrémenter le nombre total de livres chaque fois qu'un nouveau livre est créé
        Livre.nombre_livres += 1

    @staticmethod
    def afficher_nombre_livres():
        """Méthode statique pour afficher le nombre total de livres."""
        print(f"Nombre total de livres: {Livre.nombre_livres}")

    def afficher_details(self):
        """Méthode d'instance pour afficher les détails du livre."""
        print(f"Titre: {self.titre}, Auteur: {self.auteur}")
