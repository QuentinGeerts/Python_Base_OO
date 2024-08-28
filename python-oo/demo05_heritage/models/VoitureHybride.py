from models.VehiculeElectrique import VehiculeElectrique
from models.VehiculeThermique import VehiculeThermique

class VoitureHybride(VehiculeThermique, VehiculeElectrique):
    """Classe dérivée représentant une voiture hybride."""

    def __init__(self, marque, modele, annee, nombre_portes, capacite_carburant, autonomie):
        super().__init__(marque, modele, annee, capacite_carburant)
        VehiculeElectrique.__init__(self, marque, modele, annee, autonomie)
        self.nombre_portes = nombre_portes

    def description(self):
        """Méthode surchargée pour obtenir une description spécifique de la voiture hybride."""
        return f"{super().description()}, {self.nombre_portes} portes"
    
    def __str__(self):
        return f"Voiture hybride: {self.description()}"