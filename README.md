# Formation Python — Base & Orienté Objet

## Table des matières

### Python Base
1. [Variables et types](#1-variables-et-types)
2. [Console — Entrées / Sorties](#2-console--entrées--sorties)
3. [Opérateurs](#3-opérateurs)
4. [Structures conditionnelles](#4-structures-conditionnelles)
5. [Structures itératives](#5-structures-itératives)
6. [Collections](#6-collections)
7. [Fonctions et méthodes](#7-fonctions-et-méthodes)
8. [Gestion des erreurs](#8-gestion-des-erreurs)

### Python Orienté Objet
9. [Introduction à l'OO — Classes & Objets](#9-introduction-à-loo--classes--objets)
10. [Classes — Attributs & Méthodes](#10-classes--attributs--méthodes)
11. [Encapsulation](#11-encapsulation)
12. [Data Models — Méthodes spéciales](#12-data-models--méthodes-spéciales)
13. [Héritage](#13-héritage)
14. [Classes abstraites](#14-classes-abstraites)
15. [Membres statiques](#15-membres-statiques)
16. [Interfaces](#16-interfaces)

---

# PYTHON BASE

---

## 1. Variables et types

### Définition
Une **variable** est une boîte nommée qui stocke une valeur en mémoire. Python est **dynamiquement typé** : inutile de déclarer le type, Python le déduit tout seul à l'affectation.

### Types fondamentaux

| Type    | Description              | Exemple          |
|---------|--------------------------|------------------|
| `int`   | Nombre entier            | `age = 30`       |
| `float` | Nombre décimal           | `taille = 1.75`  |
| `str`   | Chaîne de caractères     | `nom = "Alice"`  |
| `bool`  | Vrai ou Faux             | `actif = True`   |

### Syntaxe
```python
nom_variable = valeur

# Déclaration multiple sur une ligne
a, b, c = 1, 2, 3
```

### Exemple
```python
age = 30
taille = 1.75
message = "Bonjour !"
est_actif = True

print(type(age))      # <class 'int'>
print(type(taille))   # <class 'float'>
print(type(message))  # <class 'str'>
print(type(est_actif))# <class 'bool'>
```

### Tips
> **Convention de nommage** : utilisez le `snake_case` (mots en minuscules séparés par `_`).
> `nombre_de_livres` est bien, `NombreDeLivres` c'est pour les classes.

> `type(variable)` vous dit toujours quel type est stocké — pratique pour déboguer !

---

## 2. Console — Entrées / Sorties

### Définition
- **Sortie** : afficher des informations à l'utilisateur avec `print()`.
- **Entrée** : lire une saisie clavier avec `input()`. Attention, `input()` retourne **toujours une chaîne** (`str`) — pensez à convertir si nécessaire.

### Syntaxe
```python
# Sortie
print(valeur1, valeur2, sep=" - ", end="\n")

# f-string (la façon la plus lisible d'insérer des variables)
print(f"Bonjour {nom}, vous avez {age} ans.")

# Entrée
variable = input("Message affiché à l'utilisateur : ")

# Conversion de type
nombre = int(input("Entrez un nombre : "))
```

### Exemple
```python
nom = input("Quel est votre nom ? ")
age = int(input("Quel est votre âge ? "))

annee_naissance = 2024 - age
print(f"Bonjour {nom}, vous êtes né(e) en {annee_naissance}.")
# → Bonjour Alice, vous êtes né(e) en 1996.
```

### Tips
> **Séparateur et fin de ligne** : `print("a", "b", sep=" - ", end="!")` affiche `a - b!`.

> **Convertisseurs courants** :
> - `int()` → entier
> - `float()` → décimal
> - `str()` → chaîne

> Si l'utilisateur entre `"abc"` et vous faites `int(input(...))`, Python lève une `ValueError`. Pensez à gérer les erreurs (voir chapitre 8) !

---

## 3. Opérateurs

### Définition
Les **opérateurs** permettent d'effectuer des calculs, des comparaisons et de combiner des conditions logiques.

### Arithmétiques

| Opérateur | Description        | Exemple        | Résultat |
|-----------|--------------------|----------------|----------|
| `+`       | Addition           | `10 + 5`       | `15`     |
| `-`       | Soustraction       | `10 - 5`       | `5`      |
| `*`       | Multiplication     | `10 * 5`       | `50`     |
| `/`       | Division réelle    | `10 / 5`       | `2.0`    |
| `//`      | Division entière   | `10 // 3`      | `3`      |
| `%`       | Modulo (reste)     | `10 % 3`       | `1`      |
| `**`      | Puissance          | `2 ** 8`       | `256`    |

### Comparaison

| Opérateur | Description           |
|-----------|-----------------------|
| `==`      | Égal à                |
| `!=`      | Différent de          |
| `>`       | Supérieur à           |
| `<`       | Inférieur à           |
| `>=`      | Supérieur ou égal à   |
| `<=`      | Inférieur ou égal à   |

### Logiques

| Opérateur | Description                       | Exemple                    |
|-----------|-----------------------------------|----------------------------|
| `and`     | Vrai si les deux sont vrais       | `True and False` → `False` |
| `or`      | Vrai si au moins un est vrai      | `True or False` → `True`   |
| `not`     | Inverse le booléen                | `not True` → `False`       |

### Exemple
```python
x, y, z = 5, 10, 15

# Vérifier si x < y ET y < z
print((x < y) and (y < z))   # True

# Vérifier si x > y OU y > z
print((x > y) or (y > z))    # False

# Division et reste
print(10 // 3)  # 3
print(10 % 3)   # 1
```

### Tips
> **Modulo** `%` est très utile pour savoir si un nombre est pair : `n % 2 == 0`.

> **Priorité** : comme en maths, `**` > `* /` > `+ -`. Utilisez des parenthèses pour clarifier.

---

## 4. Structures conditionnelles

### Définition
Une **structure conditionnelle** exécute un bloc de code uniquement si une condition est vraie. Elle permet au programme de prendre des décisions.

### Syntaxe
```python
if condition:
    # si condition est vraie
elif autre_condition:
    # si autre_condition est vraie
else:
    # dans tous les autres cas
```

### Exemple
```python
age = 14

if age >= 18:
    print("Vous êtes majeur.")
elif age >= 13:
    print("Vous êtes adolescent.")   # → affiché
else:
    print("Vous êtes enfant.")

# Conditions multiples
temperature = 25
ensoleille = True

if temperature > 20 and ensoleille:
    print("Il fait beau et chaud dehors !")

# Conditions imbriquées
note = 85

if note >= 50:
    print("Réussi !")
    if note >= 80:
        print("Avec mention bien !")  # → affiché
```

### Tips
> **Pas de `switch/case`** en Python (avant 3.10) : on enchaîne les `elif`.
> Depuis Python 3.10, il existe le `match/case` pour remplacer les longues chaînes d'`elif`.

> **Condition ternaire** (sur une ligne) :
> ```python
> statut = "majeur" if age >= 18 else "mineur"
> ```

---

## 5. Structures itératives

### Définition
Une **boucle** répète un bloc de code plusieurs fois. Python propose deux types : `for` (itération sur une séquence) et `while` (tant qu'une condition est vraie).

### Syntaxe

```python
# Boucle for — parcourir une séquence
for element in sequence:
    # traitement

# Boucle for avec range()
for i in range(debut, fin, pas):
    # traitement

# Boucle while
while condition:
    # traitement
```

### Exemple
```python
# for — parcourir une liste
fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    print(fruit)

# for avec enumerate() — obtenir index + valeur
for i, fruit in enumerate(fruits):
    print(f"Index {i} : {fruit}")

# range(0, 6, 2) → 0, 2, 4
for i in range(0, 6, 2):
    print(i)

# while
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1

# break — stopper la boucle
for i in range(10):
    if i == 5:
        break          # s'arrête à 5
    print(i)

# continue — passer à l'itération suivante
for i in range(10):
    if i % 2 == 0:
        continue       # ignore les pairs
    print(i)           # affiche uniquement les impairs
```

### Tips
> **`enumerate()`** est votre meilleur ami quand vous avez besoin de l'index ET de la valeur en même temps.

> **`range(n)`** génère les entiers de `0` à `n-1`. `range(5)` → 0, 1, 2, 3, 4.

> Attention aux **boucles infinies** avec `while` : assurez-vous que la condition finit par devenir `False` !

---

## 6. Collections

### Définition
Python propose 4 types de collections pour stocker plusieurs valeurs :

| Type   | Ordonné | Modifiable | Doublons | Syntaxe        |
|--------|---------|------------|----------|----------------|
| `list` | Oui     | Oui        | Oui      | `[1, 2, 3]`    |
| `tuple`| Oui     | Non        | Oui      | `(1, 2, 3)`    |
| `set`  | Non     | Oui        | Non      | `{1, 2, 3}`    |
| `dict` | Oui*    | Oui        | Clés non | `{"a": 1}`     |

*Les dictionnaires conservent l'ordre d'insertion depuis Python 3.7.

---

### List

```python
fruits = ["pomme", "banane", "cerise"]

fruits.append("orange")          # Ajouter à la fin
fruits.insert(1, "kiwi")         # Insérer à l'index 1
fruits.remove("banane")          # Supprimer par valeur
fruits.pop()                      # Retirer le dernier
del fruits[2]                     # Supprimer par index

# Slicing — extraire une partie
print(fruits[1:3])   # index 1 et 2
print(fruits[:3])    # du début à l'index 2
print(fruits[-1])    # dernier élément
```

> **Copie d'une liste** — attention, `liste1 = liste2` ne copie pas, elles pointent sur le même objet !
> ```python
> copie = ma_liste[:]        # copie par slicing
> copie = ma_liste.copy()    # copie avec .copy()
> copie = list(ma_liste)     # copie avec list()
> ```

---

### Tuple

```python
coordonnees = (10, 20)
print(coordonnees[0])   # 10

# Immuable : on ne peut pas modifier, mais on peut concaténer
nouvelles = coordonnees + (30, 40)
print(nouvelles)        # (10, 20, 30, 40)
```

> **Quand utiliser un tuple ?** Quand les données ne doivent pas changer : coordonnées GPS, couleur RGB, retour multiple d'une fonction.

---

### Set

```python
animaux = {"chat", "chien", "lapin"}
animaux.add("hamster")
animaux.remove("chat")
print("chien" in animaux)   # True

# Opérations ensemblistes
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)   # Union        → {1, 2, 3, 4}
print(a & b)   # Intersection → {2, 3}
print(a - b)   # Différence   → {1}
```

---

### Dictionary

```python
etudiant = {
    "nom": "Quentin",
    "age": 28,
    "cours": ["Angular", "Python"]
}

# Accès
print(etudiant["nom"])      # Quentin

# Modification
etudiant["age"] = 29

# Ajout
etudiant["ville"] = "Bruxelles"

# Suppression
del etudiant["ville"]
etudiant.pop("age")

# Itération
for cle, valeur in etudiant.items():
    print(f"{cle} : {valeur}")
```

### Tips
> **Vérifier si une clé existe** : `if "nom" in etudiant:` — évite les `KeyError`.

> **Valeur par défaut** : `etudiant.get("telephone", "Non renseigné")` retourne `"Non renseigné"` si la clé n'existe pas.

---

## 7. Fonctions et méthodes

### Définition
- **Procédure** : bloc de code réutilisable qui ne retourne **rien**.
- **Fonction** : bloc de code réutilisable qui **retourne une valeur** avec `return`.

En Python, les deux se définissent avec `def`. La distinction est conceptuelle.

### Syntaxe
```python
def nom_fonction(param1, param2, param3="valeur_defaut"):
    # traitement
    return resultat
```

### Exemple
```python
# Procédure
def saluer(nom):
    print(f"Bonjour, {nom}!")

saluer("Alice")   # Bonjour, Alice!

# Fonction
def additionner(a, b):
    return a + b

resultat = additionner(5, 3)   # 8

# Paramètre par défaut
def saluer(nom="Invité"):
    print(f"Bonjour, {nom}!")

saluer()          # Bonjour, Invité!
saluer("Bob")     # Bonjour, Bob!

# Retour multiple
def diviser_et_reste(a, b):
    return a // b, a % b

q, r = diviser_et_reste(10, 3)
print(f"Quotient: {q}, Reste: {r}")   # Quotient: 3, Reste: 1

# *args — nombre variable d'arguments
def additionner_tout(*args):
    return sum(args)

print(additionner_tout(1, 2, 3, 4))   # 10

# **kwargs — arguments nommés variables
def afficher_infos(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")

afficher_infos(nom="Alice", age=30, ville="Paris")

# Fonction passée en paramètre
def carre(n):
    return n * n

def appliquer(fonction, valeur):
    return fonction(valeur)

print(appliquer(carre, 5))   # 25

# Fonction récursive
def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n - 1)

print(factorielle(5))   # 120
```

### Passage par valeur vs référence

| Type                          | Comportement       |
|-------------------------------|--------------------|
| `int`, `str`, `float`, `bool`, `tuple` | Passage par **valeur** — l'original est inchangé |
| `list`, `dict`, `set`         | Passage par **référence** — l'original est modifié |

```python
# list → passage par référence
def ajouter(liste):
    liste.append(99)

ma_liste = [1, 2, 3]
ajouter(ma_liste)
print(ma_liste)   # [1, 2, 3, 99]  ← modifié !

# Protéger l'original
ajouter(ma_liste.copy())
print(ma_liste)   # [1, 2, 3, 99]  ← inchangé
```

### Tips
> **`*args`** reçoit les arguments positionnels sous forme de tuple.
> **`**kwargs`** reçoit les arguments nommés sous forme de dictionnaire.

> Passer une fonction sans parenthèses (`appliquer(carre, 5)`) transmet la **fonction elle-même**.
> Avec parenthèses (`appliquer(carre(5), ...)`), vous passeriez son **résultat** — ce n'est pas la même chose !

---

## 8. Gestion des erreurs

### Définition
La **gestion des erreurs** permet d'anticiper et de traiter les situations exceptionnelles sans faire planter le programme. Python utilise le bloc `try / except`.

### Syntaxe
```python
try:
    # code susceptible de planter
except TypeErreur:
    # si cette erreur précise survient
except Exception as e:
    # toute autre erreur
else:
    # si AUCUNE erreur n'a eu lieu
finally:
    # s'exécute TOUJOURS (erreur ou pas)
```

### Exemple
```python
try:
    nombre = int(input("Entrez un nombre : "))
    resultat = 10 / nombre
except ValueError:
    print("Erreur : ce n'est pas un nombre.")
except ZeroDivisionError:
    print("Erreur : division par zéro.")
except Exception as e:
    print(f"Erreur inattendue : {e}")
else:
    print(f"Résultat : {resultat}")
finally:
    print("Fin de l'opération.")

# Lever une exception manuellement
def verifier_age(age):
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif.")
    print(f"Age valide : {age}")

try:
    verifier_age(-5)
except ValueError as e:
    print(f"Erreur capturée : {e}")
```

### Erreurs courantes

| Exception           | Cause typique                              |
|---------------------|--------------------------------------------|
| `ValueError`        | Mauvaise conversion (`int("abc")`)         |
| `ZeroDivisionError` | Division par zéro                          |
| `IndexError`        | Index hors limites sur une liste           |
| `KeyError`          | Clé inexistante dans un dictionnaire       |
| `TypeError`         | Mauvais type passé à une opération         |
| `AttributeError`    | Attribut inexistant sur un objet           |

### Tips
> **`finally`** est parfait pour libérer des ressources : fermer un fichier, déconnecter une base de données, etc.

> **`raise`** permet de déclencher une exception volontairement pour signaler qu'une valeur est invalide.

> Ne capturez **jamais** `Exception` de manière silencieuse sans au moins afficher l'erreur — vous masqueriez des bugs.

---

# PYTHON ORIENTÉ OBJET

---

## 9. Introduction à l'OO — Classes & Objets

### Définition
La **Programmation Orientée Objet (POO)** structure le code autour d'**objets** qui regroupent des données (attributs) et des comportements (méthodes).

- **Classe** : le plan, le moule (ex : le plan d'une voiture).
- **Objet / Instance** : un exemplaire concret créé à partir du moule (ex : ma Kia Ceed).
- **Constructeur** `__init__` : méthode appelée automatiquement à la création d'un objet.
- **`self`** : référence à l'instance en cours — obligatoire comme premier paramètre de toute méthode d'instance.

### Syntaxe
```python
class NomClasse:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
```

### Exemple
```python
class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

# Créer des instances
voiture1 = Voiture("Kia", "Ceed GT-Line")
print(voiture1.marque)    # Kia
print(voiture1.modele)    # Ceed GT-Line
```

### Tips
> Le nom d'une classe commence par une **majuscule** (`PascalCase`).

> `self` n'est pas un mot-clé réservé mais c'est la **convention universelle** — ne le remplacez pas.

---

## 10. Classes — Attributs & Méthodes

### Définition
Une **méthode d'instance** est une fonction définie dans une classe. Elle reçoit toujours `self` en premier paramètre et peut accéder aux attributs de l'instance.

### Syntaxe
```python
class NomClasse:
    def __init__(self, ...):
        self.attribut = valeur

    def ma_methode(self):
        # traitement avec self.attribut
        print(...)
```

### Exemple
```python
class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def afficher_details(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}")

voiture = Voiture("Kia", "Ceed GT-Line")
voiture.afficher_details()
# → Marque: Kia, Modèle: Ceed GT-Line
```

### Tips
> Chaque méthode d'instance **doit** avoir `self` comme premier paramètre, même si vous ne l'utilisez pas dans le corps.

> Les attributs définis dans `__init__` avec `self.` sont accessibles depuis toutes les méthodes de la classe.

---

## 11. Encapsulation

### Définition
L'**encapsulation** consiste à contrôler l'accès aux attributs et méthodes d'une classe. Python utilise des conventions de nommage :

| Préfixe | Visibilité  | Description                              |
|---------|-------------|------------------------------------------|
| Aucun   | Public      | Accessible de partout                    |
| `_`     | Protected   | Usage interne — accessible mais déconseillé depuis l'extérieur |
| `__`    | Private     | Accessible uniquement dans la classe     |

### Syntaxe
```python
class MaClasse:
    def __init__(self):
        self.public = "visible partout"
        self._protege = "usage interne"
        self.__prive = "uniquement dans la classe"
```

### Exemple
```python
class CompteBancaire:
    def __init__(self, titulaire, solde_initial):
        self.titulaire = titulaire       # public
        self._solde = solde_initial      # protégé
        self.__historique = []           # privé

    def deposer(self, montant):
        if montant > 0:
            self._solde += montant
            self.__ajouter_transaction(f"Dépôt: {montant}€")

    def retirer(self, montant):
        if 0 < montant <= self._solde:
            self._solde -= montant
            self.__ajouter_transaction(f"Retrait: {montant}€")

    def afficher_solde(self):
        print(f"Solde de {self.titulaire} : {self._solde}€")

    def _calculer_interet(self):         # méthode protégée
        return self._solde * 0.05

    def __ajouter_transaction(self, desc): # méthode privée
        self.__historique.append(desc)

compte = CompteBancaire("Alice", 1000)
compte.deposer(500)
compte.retirer(200)
compte.afficher_solde()
# → Solde de Alice : 1300€

# print(compte.__historique)  ← AttributeError !
```

### Tips
> **`__` (double underscore)** déclenche le *name mangling* : l'attribut `__historique` est renommé en `_CompteBancaire__historique` en interne. Inatteignable directement de l'extérieur.

> En Python, l'encapsulation est une **convention** (pas une barrière absolue comme en Java/C#). On fait confiance aux développeurs pour respecter `_` et `__`.

---

## 12. Data Models — Méthodes spéciales

### Définition
Les **méthodes spéciales** (ou "dunder methods", de *double underscore*) permettent de personnaliser le comportement des objets en réponse à des opérations Python standard (`print`, `repr`, `del`, etc.).

### Méthodes spéciales courantes

| Méthode       | Rôle                                              |
|---------------|---------------------------------------------------|
| `__init__`    | Constructeur                                      |
| `__str__`     | Représentation lisible (`str(obj)`, `print(obj)`) |
| `__repr__`    | Représentation technique (débogage)               |
| `__getattr__` | Appelé quand un attribut est introuvable          |
| `__setattr__` | Appelé à chaque affectation d'attribut            |
| `__delattr__` | Appelé lors de `del obj.attr`                     |

### Attributs spéciaux

| Attribut       | Contenu                             |
|----------------|-------------------------------------|
| `obj.__class__`  | La classe de l'objet              |
| `obj.__dict__`   | Dictionnaire des attributs        |
| `obj.__doc__`    | Docstring de la classe            |
| `obj.__module__` | Module où la classe est définie   |

### Exemple
```python
class Voiture:
    """Classe représentant une voiture."""

    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.__annee = 2024

    def __str__(self):
        return f"{self.marque} {self.modele}"

    def __repr__(self):
        return f"Voiture(marque='{self.marque}', modele='{self.modele}')"

    def __getattr__(self, attr):
        if attr == "annee":
            return self.__annee

    def __setattr__(self, attr, valeur):
        if attr == "annee":
            if isinstance(valeur, int) and 1900 <= valeur <= 2024:
                self.__dict__[attr] = valeur
            else:
                raise ValueError("Année invalide.")
        else:
            super().__setattr__(attr, valeur)

    def __delattr__(self, attr):
        if attr == "annee":
            raise AttributeError("Année ne peut pas être supprimée.")
        else:
            super().__delattr__(attr)

v = Voiture("Kia", "Ceed")
print(str(v))    # Kia Ceed
print(repr(v))   # Voiture(marque='Kia', modele='Ceed')
print(v.__doc__) # Classe représentant une voiture.
print(v.__dict__)# {'marque': 'Kia', 'modele': 'Ceed'}
```

### Tips
> **`__str__`** est pour l'affichage final (utilisateur). **`__repr__`** est pour le débogage (développeur).

> Si vous ne définissez que l'un des deux, Python utilisera `__repr__` en fallback.

---

## 13. Héritage

### Définition
L'**héritage** permet à une classe **enfant** de réutiliser les attributs et méthodes d'une classe **parent**, tout en pouvant les modifier ou les étendre.

- **Classe parent / base** : la classe dont on hérite.
- **Classe enfant / dérivée** : la classe qui hérite.
- **`super()`** : appelle la méthode du parent.
- **Surcharge** (*override*) : redéfinir une méthode du parent dans l'enfant.
- **Héritage multiple** : une classe peut hériter de plusieurs parents.

### Syntaxe
```python
class Enfant(Parent):
    def __init__(self, ...):
        super().__init__(...)   # appel du constructeur parent
        self.attribut_enfant = valeur
```

### Exemple
```python
class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def demarrer(self):
        return "Le véhicule démarre."

    def description(self):
        return f"{self.marque} {self.modele} ({self.annee})"

    def __str__(self):
        return f"Véhicule: {self.description()}"


class VehiculeElectrique(Vehicule):
    def __init__(self, marque, modele, annee, autonomie):
        super().__init__(marque, modele, annee)
        self.autonomie = autonomie

    def description(self):   # surcharge
        return f"{super().description()}, autonomie: {self.autonomie} km"

    def recharger(self):
        return "Le véhicule se recharge."


class VehiculeThermique(Vehicule):
    def __init__(self, marque, modele, annee, capacite_carburant):
        super().__init__(marque, modele, annee)
        self.capacite_carburant = capacite_carburant


# Héritage multiple
class VoitureHybride(VehiculeThermique, VehiculeElectrique):
    def __init__(self, marque, modele, annee, portes, carburant, autonomie):
        VehiculeThermique.__init__(self, marque, modele, annee, carburant)
        VehiculeElectrique.__init__(self, marque, modele, annee, autonomie)
        self.nombre_portes = portes


ve = VehiculeElectrique("Tesla", "Model 3", 2023, 580)
print(ve.demarrer())        # Le véhicule démarre. (hérité)
print(ve.description())     # Tesla Model 3 (2023), autonomie: 580 km (surchargé)
```

### Tips
> **MRO** (*Method Resolution Order*) : en héritage multiple, Python cherche la méthode de gauche à droite dans la liste des parents. `VoitureHybride(VehiculeThermique, VehiculeElectrique)` → cherche d'abord dans `VehiculeThermique`.

> `super()` est préféré à `NomParent.__init__(self, ...)` car il respecte le MRO automatiquement.

---

## 14. Classes abstraites

### Définition
Une **classe abstraite** est une classe **incomplète** qui définit un contrat : elle déclare des méthodes obligatoires que toutes ses classes filles devront implémenter. On ne peut pas instancier directement une classe abstraite.

Python utilise le module `abc` (*Abstract Base Classes*).

### Syntaxe
```python
from abc import ABC, abstractmethod

class MaClasseAbstraite(ABC):
    @abstractmethod
    def ma_methode(self):
        pass
```

### Exemple
```python
from abc import ABC, abstractmethod
import math

class Forme(ABC):
    """Classe abstraite — définit le contrat pour toutes les formes."""

    @property
    @abstractmethod
    def nom(self):
        pass

    @abstractmethod
    def aire(self):
        pass

    @abstractmethod
    def perimetre(self):
        pass

    def __str__(self):
        return f"{self.nom}: aire={self.aire():.2f}, périmètre={self.perimetre():.2f}"


class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
        self._nom = "Cercle"

    @property
    def nom(self):
        return self._nom

    def aire(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self._nom = "Rectangle"

    @property
    def nom(self):
        return self._nom

    def aire(self):
        return self.largeur * self.hauteur

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)


cercle = Cercle(5)
rectangle = Rectangle(4, 7)
print(cercle)     # Cercle: aire=78.54, périmètre=31.42
print(rectangle)  # Rectangle: aire=28, périmètre=22

# Forme()  ← TypeError : impossible d'instancier une classe abstraite
```

### Tips
> Si une classe fille n'implémente pas **toutes** les méthodes abstraites, elle devient elle-même abstraite et ne peut pas être instanciée.

> Combiner `@property` et `@abstractmethod` force les classes filles à implémenter la propriété (pas juste une méthode).

---

## 15. Membres statiques

### Définition
Un **attribut statique** (ou de classe) est partagé par **toutes les instances** d'une classe. Une **méthode statique** (`@staticmethod`) n'a pas accès à `self` ni à la classe — c'est une simple fonction attachée à la classe.

### Syntaxe
```python
class MaClasse:
    attribut_statique = 0   # partagé par toutes les instances

    @staticmethod
    def ma_methode_statique():
        # pas de self, pas de cls
        pass
```

### Exemple
```python
class Livre:
    nombre_livres = 0   # attribut statique

    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        Livre.nombre_livres += 1   # incrément partagé

    def afficher_details(self):
        print(f"Titre: {self.titre}, Auteur: {self.auteur}")

    @staticmethod
    def afficher_nombre_livres():
        print(f"Nombre total de livres: {Livre.nombre_livres}")


livre1 = Livre("Le Petit Prince", "Saint-Exupéry")
livre2 = Livre("1984", "George Orwell")
livre3 = Livre("Moby Dick", "Herman Melville")

livre1.afficher_details()          # Titre: Le Petit Prince, Auteur: Saint-Exupéry
Livre.afficher_nombre_livres()     # Nombre total de livres: 3

# Accessible aussi via l'instance (mais moins lisible)
livre1.afficher_nombre_livres()    # Nombre total de livres: 3
print(Livre.nombre_livres)         # 3
```

### Tips
> **Accédez aux attributs statiques via la classe** (`Livre.nombre_livres`) plutôt que via l'instance (`livre1.nombre_livres`). C'est plus clair et évite les confusions si vous écrasez accidentellement la valeur sur une instance.

> Il existe aussi `@classmethod` qui reçoit `cls` (la classe elle-même) en premier paramètre — utile pour créer des constructeurs alternatifs.

---

## 16. Interfaces

### Définition
Python n'a pas de mot-clé `interface` comme Java ou C#. On simule les interfaces avec des **classes abstraites** (`ABC`) dont **toutes les méthodes sont abstraites**. L'interface définit un contrat sans aucune logique — les classes concrètes doivent tout implémenter.

**Différence classe abstraite / interface :**
- **Classe abstraite** : peut avoir des méthodes concrètes (avec logique) ET abstraites.
- **Interface** (simulée) : uniquement des méthodes abstraites — aucune logique.

### Syntaxe
```python
from abc import ABC, abstractmethod

class MonInterface(ABC):
    @abstractmethod
    def methode_a(self):
        pass

    @abstractmethod
    def methode_b(self):
        pass
```

### Exemple
```python
from abc import ABC, abstractmethod

class GestionPaiement(ABC):
    """Interface — contrat pour tout système de paiement."""

    @abstractmethod
    def traiter_paiement(self, montant):
        pass

    @abstractmethod
    def obtenir_statut(self):
        pass


class PaiementCarte(GestionPaiement):
    def __init__(self, titulaire, numero_carte):
        self.titulaire = titulaire
        self.numero_carte = numero_carte
        self.statut = "Non traité"

    def traiter_paiement(self, montant):
        if montant > 0:
            self.statut = "Traitement réussi"
            print(f"Paiement de {montant}€ traité par carte.")
        else:
            self.statut = "Échec"
            print("Montant invalide.")

    def obtenir_statut(self):
        return self.statut


class PaiementPayPal(GestionPaiement):
    def __init__(self, compte_email):
        self.compte_email = compte_email
        self.statut = "Non traité"

    def traiter_paiement(self, montant):
        if montant > 0:
            self.statut = "Traitement réussi"
            print(f"Paiement de {montant}€ traité via PayPal.")
        else:
            self.statut = "Échec"
            print("Montant invalide.")

    def obtenir_statut(self):
        return self.statut


# Polymorphisme — même interface, comportements différents
paiements = [
    PaiementCarte("Jean Dupont", "1234 5678 9012 3456"),
    PaiementPayPal("jean@example.com")
]

for paiement in paiements:
    paiement.traiter_paiement(100)
    print(paiement.obtenir_statut())
```

### Tips
> **Polymorphisme** : grâce à l'interface, vous pouvez traiter `PaiementCarte` et `PaiementPayPal` de la même façon — votre code ne dépend pas de l'implémentation concrète.

> Une classe peut implémenter **plusieurs interfaces** en héritant de plusieurs classes ABC :
> ```python
> class MaClasse(Interface1, Interface2):
>     ...
> ```

---

## Récapitulatif — Les 4 piliers de l'OO

| Pilier           | Définition courte                                           | Chapitre |
|------------------|-------------------------------------------------------------|----------|
| **Encapsulation**| Cacher et protéger les données internes                     | 11       |
| **Héritage**     | Réutiliser et étendre le comportement d'une classe parente  | 13       |
| **Abstraction**  | Définir un contrat sans détail d'implémentation             | 14, 16   |
| **Polymorphisme**| Utiliser une interface commune pour des comportements variés| 16       |

---

*Formation Python Base & OO — Support de cours*
