from models.Vehicule import Vehicule

class VehiculeElectrique(Vehicule):
    """Classe dérivée représentant un véhicule électrique."""

    def __init__(self, marque, modele, annee, autonomie):
        super().__init__(marque, modele, annee)
        self.autonomie = autonomie

    def description(self):
        """Méthode surchargée pour obtenir une description spécifique du véhicule électrique."""
        return f"{super().description()}, autonomie: {self.autonomie} km"

    def recharger(self):
        """Méthode spécifique aux véhicules électriques pour se recharger."""
        return "Le véhicule est en train de se recharger."

    def __str__(self):
        return f"Véhicule Électrique: {self.description()}"