# Sortie

# Afficher une simple chaîne de caractères
print("Bonjour, Python!")  # Affiche: Bonjour, Python!

# Afficher des variables
nom = "Alice"
age = 30
print("Nom:", nom)  # Affiche: Nom: Alice
print("Âge:", age)  # Affiche: Âge: 30

# Afficher des expressions et des résultats de calculs
print("La somme de 5 et 3 est", 5 + 3)  # Affiche: La somme de 5 et 3 est 8

# Utiliser des chaînes formatées pour afficher des messages plus complexes
print(f"{nom} a {age} ans.")  # Affiche: Alice a 30 ans.

# Modification du séparateur et caractères de fin de ligne

print ("Ceci", "est", "une", "chaine", sep=" - ", end="❤️")


# Entrée

# Demander le nom de l'utilisateur et le stocker dans la variable 'nom'
nom = input("Quel est votre nom ? ")
print("Bonjour,", nom)  # Affiche: Bonjour, Quentin

# Demander l'âge de l'utilisateur
age = input("Quel est votre âge ? ")
print(f"Vous avez {age} ans.")  # Affiche: Vous avez 28 ans.

# Conversion de type

# Lire un nombre de l'utilisateur et le convertir en entier
nombre = input("Entrez un nombre : ")
nombre = int(nombre)  # Conversion de la chaîne de caractères en entier

# int() => int
# float() => float
# str() => string

# Effectuer un calcul avec le nombre
carre = nombre ** 2
print(f"Le carré de {nombre} est {carre}.")  # Affiche: Le carré de [nombre] est [carré].

# Demander des informations à l'utilisateur
nom = input("Quel est votre nom ? ")
age = int(input("Quel est votre âge ? "))

# Calculer l'année de naissance
annee_actuelle = 2024
annee_naissance = annee_actuelle - age

# Afficher un message à l'utilisateur
print(f"Bonjour {nom}, vous êtes né(e) en {annee_naissance}.")
