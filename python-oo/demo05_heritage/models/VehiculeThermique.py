from models.Vehicule import Vehicule

class VehiculeThermique(Vehicule):
    """Classe dérivée représentant un véhicule thermique"""

    def __init__(self, marque, modele, annee, capacite_carburant):
        Vehicule.__init__(self, marque, modele, annee)
        self.capacite_carburant = capacite_carburant

    def description(self):
        """Méthode surchargée pour obtenir une description spécifique du véhicule thermique."""
        return f"{super().description()}, capacité carburant: {self.capacite_carburant} L"

    def __str__(self):
        return f"Véhicule thermique: {self.description()}"