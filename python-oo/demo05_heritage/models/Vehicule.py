class Vehicule:
    """Classe de base représentant un véhicule."""
    
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def description(self):
        """Méthode pour obtenir une description générale du véhicule."""
        return f"{self.marque} {self.modele} ({self.annee})"

    def demarrer(self):
        """Méthode pour démarrer le véhicule."""
        return "Le véhicule démarre."
    
    def klaxonner(self):
        """Méthode spécifique aux voitures pour klaxonner."""
        return "La voiture klaxonne : Bip bip !"

    def __str__(self):
        return f"Véhicule: {self.description()}"