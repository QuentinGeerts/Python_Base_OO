from models.Livre import Livre

# Création d'instances de livres
livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
livre2 = Livre("1984", "George Orwell")
livre3 = Livre("Moby Dick", "Herman Melville")

# Utilisation des méthodes d'instance
livre1.afficher_details()   # Affiche: Titre: Le Petit Prince, Auteur: Antoine de Saint-Exupéry
livre2.afficher_details()   # Affiche: Titre: 1984, Auteur: George Orwell

# Utilisation de la méthode statique
Livre.afficher_nombre_livres()  # Affiche: Nombre total de livres: 3

# Utilisation de la méthode statique via une instance (pas recommandé mais possible)
livre3.afficher_nombre_livres()  # Affiche: Nombre total de livres: 3

# Récupération par l'attribut statique (via la classe)
print("Nombre de livres:", Livre.nombre_livres)

# Récupération par l'attribut statique (via l'instance)
print("Nombre de livres:", livre3.nombre_livres)