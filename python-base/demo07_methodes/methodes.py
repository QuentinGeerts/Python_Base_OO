# Méthodes

# Procédure : Ne retourne rien
# Fonction   : Retourne une valeur


# ─────────────────────────────────────────────
# 1. Procédure simple (sans argument, sans retour)
# ─────────────────────────────────────────────

def saluer():
    print("Bonjour tout le monde!")

saluer()  # Affiche: Bonjour tout le monde!


# ─────────────────────────────────────────────
# 2. Procédure avec argument
# ─────────────────────────────────────────────

def saluer_utilisateur(nom):
    print(f"Bonjour, {nom}!")

saluer_utilisateur("Alice")  # Affiche: Bonjour, Alice!


# ─────────────────────────────────────────────
# 3. Fonction avec valeur de retour
# ─────────────────────────────────────────────

def additionner(a, b):
    return a + b

resultat = additionner(5, 3)
print(resultat)  # Affiche: 8


# ─────────────────────────────────────────────
# 4. Fonction avec paramètre par défaut
# ─────────────────────────────────────────────

def saluer_utilisateur(nom="Invité"):
    print(f"Bonjour, {nom}!")

saluer_utilisateur()        # Affiche: Bonjour, Invité!
saluer_utilisateur("Bob")   # Affiche: Bonjour, Bob!


# ─────────────────────────────────────────────
# 5. Fonction avec plusieurs valeurs de retour
# ─────────────────────────────────────────────

def diviser_et_reste(a, b):
    quotient = a // b
    reste = a % b
    return quotient, reste

q, r = diviser_et_reste(10, 3)
print(f"Quotient: {q}, Reste: {r}")  # Affiche: Quotient: 3, Reste: 1


# ─────────────────────────────────────────────
# 6. Fonction qui appelle une autre fonction
# ─────────────────────────────────────────────

def carre(n):
    return n * n

def somme_des_carres(a, b):
    return carre(a) + carre(b)

print(somme_des_carres(3, 4))  # Affiche: 25


# ─────────────────────────────────────────────
# 7. Passage par valeur vs passage par référence
# ─────────────────────────────────────────────

# Types immuables (int, str, float, bool, tuple) → passage par VALEUR
#   → la fonction reçoit une copie, l'original est inchangé

# Types mutables (list, dict, set) → passage par RÉFÉRENCE
#   → la fonction reçoit l'original, les modifications sont permanentes


# - Passage par valeur (int)

def doubler(n):
    n = n * 2
    print(f"Dans la fonction : {n}")

nombre = 10
doubler(nombre)
print(f"Après l'appel : {nombre}")  # Affiche: 10 ← inchangé


# - Passage par valeur (str)

def mettre_en_majuscules(texte):
    texte = texte.upper()
    print(f"Dans la fonction : {texte}")

mot = "bonjour"
mettre_en_majuscules(mot)
print(f"Après l'appel : {mot}")  # Affiche: bonjour ← inchangé


# - Passage par référence (list)

def ajouter_element(liste):
    liste.append(99)

ma_liste = [1, 2, 3]
ajouter_element(ma_liste)
print(ma_liste)  # Affiche: [1, 2, 3, 99] ← modifié !


# - Passage par référence (dict)

def mettre_a_jour_age(personne):
    personne["age"] = 99

utilisateur = {"nom": "Alice", "age": 30}
mettre_a_jour_age(utilisateur)
print(utilisateur)  # Affiche: {'nom': 'Alice', 'age': 99} ← modifié !


# - Protéger l'original avec une copie

def ajouter_element(liste):
    liste.append(99)

ma_liste = [1, 2, 3]
ajouter_element(ma_liste.copy())  # On passe une copie
print(ma_liste)  # Affiche: [1, 2, 3] ← inchangé !


# ─────────────────────────────────────────────
# 8. Fonction avec un nombre variable d'arguments (*args)
# ─────────────────────────────────────────────

def additionner_tout(*args):
    total = 0
    for nombre in args:
        total += nombre
    return total

print(additionner_tout(1, 2, 3))      # Affiche: 6
print(additionner_tout(10, 20, 30))   # Affiche: 60


# ─────────────────────────────────────────────
# 9. Fonction avec des arguments nommés (**kwargs)
# ─────────────────────────────────────────────

def afficher_infos(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")

afficher_infos(nom="Alice", age=30, ville="Paris")
# Affiche:
# nom: Alice
# age: 30
# ville: Paris


# ─────────────────────────────────────────────
# 10. Combiner *args et **kwargs
# ─────────────────────────────────────────────

def afficher_tout(*args, **kwargs):
    for valeur in args:
        print(valeur)
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")

afficher_tout("Python", "Java", langage_prefere="Python", niveau="débutant")
# Affiche:
# Python
# Java
# langage_prefere: Python
# niveau: débutant


# ─────────────────────────────────────────────
# 11. Passer une fonction en paramètre d'une autre
# ─────────────────────────────────────────────

# En Python, une fonction est un objet comme une variable.
# On peut donc la passer en argument à une autre fonction.

# ⚠️ On passe le nom SANS parenthèses → on passe la fonction elle-même
#    Avec parenthèses → on passerait son résultat


# - Exemple simple

def carre(n):
    return n * n

def appliquer(fonction, valeur):
    return fonction(valeur)

print(appliquer(carre, 5))   # Affiche: 25
print(appliquer(carre, 10))  # Affiche: 100


# - Avec plusieurs fonctions interchangeables

def doubler(n):
    return n * 2

def tripler(n):
    return n * 3

def appliquer(fonction, valeur):
    return fonction(valeur)

print(appliquer(doubler, 7))  # Affiche: 14
print(appliquer(tripler, 7))  # Affiche: 21


# - Appliquer une fonction sur une liste entière

def carre(n):
    return n * n

def appliquer_sur_liste(fonction, liste):
    resultats = []
    for element in liste:
        resultats.append(fonction(element))
    return resultats

nombres = [1, 2, 3, 4, 5]
print(appliquer_sur_liste(carre, nombres))   # Affiche: [1, 4, 9, 16, 25]
print(appliquer_sur_liste(doubler, nombres)) # Affiche: [2, 4, 6, 8, 10]


# ─────────────────────────────────────────────
# 12. Fonction récursive
# ─────────────────────────────────────────────

# Une fonction récursive est une fonction qui s'appelle elle-même

def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n - 1)

print(factorielle(5))  # Affiche: 120  (5 x 4 x 3 x 2 x 1)
