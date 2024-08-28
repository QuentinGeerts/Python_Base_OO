# Les collections 


#
# List
#

# Les listes sont des collections ordonnées, modifiables et qui peuvent contenir des éléments de différents types.

# Création d'une liste
fruits = ["pomme", "banane", "cerise"]

# Accéder à un élément
print(fruits[1])  # Affiche: banane

# Ajouter un élément à la fin
fruits.append("orange")
print(fruits)  # Affiche: ['pomme', 'banane', 'cerise', 'orange']

# Insérer un élément à une position spécifique
fruits.insert(1, "kiwi")
print(fruits)  # Affiche: ['pomme', 'kiwi', 'banane', 'cerise', 'orange']

# Supprimer un élément
fruits.remove("banane")
print(fruits)  # Affiche: ['pomme', 'kiwi', 'cerise', 'orange']

# Retirer un élément à la fin
fruits.pop()  # Affiche: ['pomme', 'kiwi', 'cerise']

# Supprimer un élément par son indice
del fruits[2]
print(fruits)  # Affiche: ['pomme', 'kiwi']

# Itérer sur une liste
for fruit in fruits:
    print(fruit)

fruits = ["pomme", "banane", "cerise", "poire", "ananas", "litchi"]

print("fruits[1]", fruits[1]) # pomme
print("fruits[1:3]", fruits[1:3]) # [pomme, banane]
print("fruits[:3]", fruits[:3]) # ['pomme', 'banane', 'cerise']
print("fruits[3:]", fruits[3:]) # ['poire', 'ananas', 'litchi']
print("fruits[-2]", fruits[-2]) # ananas

# Copier une liste

fruits1 = fruits
fruits2 = fruits[:]
fruits3 = fruits.copy()
fruits4 = list(fruits)

print("fruits", fruits)
print("fruits1", fruits1)
print("fruits2", fruits2)
print("fruits3", fruits3)
print("fruits4", fruits4)

print("fruit1 = fruit ?", fruits1 is fruits)
print("fruit2 = fruit ?", fruits2 is fruits)
print("fruit3 = fruit ?", fruits3 is fruits)
print("fruit4 = fruit ?", fruits4 is fruits)


#
# Tuple
# 

# Les tuples sont des collections ordonnées et immuables. Une fois créés, leurs éléments ne peuvent pas être modifiés.

# Création d'un tuple
coordonnees = (10, 20)

# Accéder à un élément
print(coordonnees[0])  # Affiche: 10

# Les tuples sont immuables, donc aucune méthode pour ajouter ou supprimer des éléments
# Vous pouvez toutefois créer un nouveau tuple en concatenant
coordonnees_nouvelles = coordonnees + (30, 40)
print(coordonnees_nouvelles)  # Affiche: (10, 20, 30, 40)

# Itérer sur un tuple
for coord in coordonnees:
    print(coord)


# 
# Set
# 

# Les ensembles (set) sont des collections non ordonnées d'éléments uniques.

# Création d'un ensemble
animaux = {"chat", "chien", "lapin"}

# Ajouter un élément
animaux.add("hamster")
print(animaux)  # Affiche: {'hamster', 'chat', 'chien', 'lapin'}

# Ajouter plusieurs élément
animaux.update(["lion", "renard"]) 
print(animaux) # Affiche: {'chat', 'chien', 'renard', 'hamster', 'lapin', 'lion'}

# Supprimer un élément
animaux.remove("chat")
print(animaux)  # Affiche: {'hamster', 'chien', 'lapin'}

# Vérifier si un élément est dans l'ensemble
print("chien" in animaux)  # Affiche: True

# Opérations sur les ensembles
ensemble1 = {1, 2, 3}
ensemble2 = {2, 3, 4}

# Union
print(ensemble1 | ensemble2)  # Affiche: {1, 2, 3, 4}

# Intersection
print(ensemble1 & ensemble2)  # Affiche: {2, 3}

# Différence
print(ensemble1 - ensemble2)  # Affiche: {1}


#
# Dictionaries
# 

# Les dictionnaires (dict) sont des collections non ordonnées de paires clé-valeur.

# Création d'un dictionnaire
etudiant = {
    "nom": "Quentin",
    "age": 28,
    "cours": ["Angular", "Informatique"]
}

# Utilisation du constructeur
etudiant2 = dict(
    nom = "Geerts",
    age = 25,
    cours = ["C#", "SQL Server"]
)

# Accéder à une valeur par sa clé
print(etudiant["nom"])  # Affiche: Quentin
print(etudiant2["nom"])  # Affiche: Geerts

# Modifier une valeur
etudiant["age"] = 22
print(etudiant["age"])  # Affiche: 22

# Ajouter une nouvelle paire clé-valeur
etudiant["adresse"] = "123 Rue Principale"
print(etudiant)

# Supprimer une paire clé-valeur
del etudiant["adresse"]
print(etudiant)

# Supprimer un élément
etudiant.pop("age")
etudiant.popitem()
print("etudiant", etudiant)

# Supprimer toutes les paires 
etudiant.clear()
print("etudiant", etudiant)

# Itérer sur les clés et les valeurs
for cle, valeur in etudiant2.items():
    print(cle, ":", valeur)

