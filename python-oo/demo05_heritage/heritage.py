from models.Vehicule import Vehicule
from models.VehiculeElectrique import VehiculeElectrique
from models.VehiculeThermique import VehiculeThermique
from models.VoitureHybride import VoitureHybride


vehicule = Vehicule('VehiculeMarque', 'VehiculeModele', 2024)
print(vehicule.demarrer())
print(vehicule.klaxonner());
print(vehicule)

vehiculeElectrique = VehiculeElectrique('VEMarque', 'VEModele', 2023, 500)
print(vehiculeElectrique.demarrer())
print(vehiculeElectrique.klaxonner());
print(vehiculeElectrique)

vehiculeThermique = VehiculeThermique('VTMarque', 'VTModele', 2022, 70)
print(vehiculeThermique.demarrer())
print(vehiculeThermique.klaxonner());
print(vehiculeThermique)

voitureHybride = VoitureHybride('VHMarque', 'VHModele', 2020, 5, 60, 600)
print(voitureHybride.demarrer())
print(voitureHybride.klaxonner());
print(voitureHybride)