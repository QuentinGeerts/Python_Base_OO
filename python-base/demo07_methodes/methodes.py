# Méthodes

# Procédure : Ne retourne rien
# Fonction : Retourne une valeur

# 1. Fonction simple sans argument

def saluer():
    print("Bonjour tout le monde!")

# Appel de la fonction
saluer()


# 2. Fonction avec arguments

def saluer_utilisateur(nom):
    print(f"Bonjour, {nom}!")

# Appel de la fonction avec un argument
saluer_utilisateur("Alice")


# 3. Fonction avec valeur de retour

def additionner(a, b):
    return a + b

# Appel de la fonction et stockage du résultat
resultat = additionner(5, 3)
print(resultat)  # Affiche: 8


# 4. Fonction avec paramètres par défaut

def saluer_utilisateur(nom="Invité"):
    print(f"Bonjour, {nom}!")

# Appel de la fonction sans argument
saluer_utilisateur()  # Affiche: Bonjour, Invité!

# Appel de la fonction avec un argument
saluer_utilisateur("Bob")  # Affiche: Bonjour, Bob!


# 5. Fonction avec plusieurs retours

def diviser_et_reste(a, b):
    quotient = a // b
    reste = a % b
    return quotient, reste

# Appel de la fonction et décomposition des résultats
q, r = diviser_et_reste(10, 3)
print(f"Quotient: {q}, Reste: {r}")  # Affiche: Quotient: 3, Reste: 1


# 6. Fonction avec des arguments variables

# - Avec *args (nombre indéterminé d'arguments)
def additionner_tout(*args):
    return sum(args)

# Appel de la fonction avec un nombre variable d'arguments
print(additionner_tout(1, 2, 3, 4))  # Affiche: 10
print(additionner_tout(10, 20))  # Affiche: 30

# - Avec **kwargs (nombre indéterminé d'arguments nommés)
def afficher_infos(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")

# Appel de la fonction avec des arguments nommés
afficher_infos(nom="Alice", age=30, ville="Paris")
