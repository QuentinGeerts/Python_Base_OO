# Structure conditionnelle


# Structure de base "if"

"""
if condition:
  # Bloc de code à exécuter si la condition est vraie
"""

age = 18

if age >= 18:
    print("Vous êtes majeur.")  # Affiche: Vous êtes majeur.


# Structure "if" avec "else"

"""
if condition:
    # Bloc de code à exécuter si la condition est vraie
else:
    # Bloc de code à exécuter si la condition est fausse
"""

age = 16

if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")  # Affiche: Vous êtes mineur.

# Structure "if", "elif" et "else"

""""
if condition1:
    # Bloc de code à exécuter si condition1 est vraie
elif condition2:
    # Bloc de code à exécuter si condition2 est vraie
elif condition3:
    # Bloc de code à exécuter si condition3 est vraie
else:
    # Bloc de code à exécuter si toutes les conditions sont fausses
"""

age = 14

if age >= 18:
    print("Vous êtes majeur.")
elif age >= 13:
    print("Vous êtes adolescent.")  # Affiche: Vous êtes adolescent.
else:
    print("Vous êtes enfant.")

# Utilisation de conditions multiples avec les opérateurs logiques

temperature = 25
ensoleille = True

if temperature > 20 and ensoleille:
    print("Il fait beau et chaud dehors.")  # Affiche: Il fait beau et chaud dehors.
elif temperature > 20 or ensoleille:
    print("Il fait chaud ou il y a du soleil.")
else:
    print("Il fait froid et il n'y a pas de soleil.")

# Imbrication des structures conditionnelles

note = 85

if note >= 50:
    print("Vous avez réussi l'examen.")
    if note >= 80:
        print("Avec mention bien !")  # Affiche: Avec mention bien !
else:
    print("Vous avez échoué l'examen.")
