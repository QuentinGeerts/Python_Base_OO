from models.Voiture import Voiture

# Création d'une instance de Voiture
v = Voiture("Kia", "Ceed")

# Utilisation des attributs spéciaux
print(v.__class__)       # Affiche: <class '__main__.Voiture'>
print(v.__dict__)        # Affiche: {'marque': 'Kia', 'modele': 'Ceed'}
print(v.__doc__)         # Affiche: Classe représentant une voiture.
print(v.__module__)      # Affiche: '__main__'
print(v.__annotations__) # Affiche: {}

# Utilisation des méthodes spéciales
print(repr(v))           # Affiche: Voiture(marque='Kia', modele='Ceed')
print(str(v))            # Affiche: Kia Ceed

# Accès via __getattr__
print(v.annee)           # Affiche: 2024

# Modification via __setattr__
v.annee = 2023
print(v.annee)           # Affiche: 2023

# Tentative de suppression d'attribut
try:
    del v.annee
except AttributeError as e:
    print(e)            # Affiche: Année ne peut pas être supprimée.
