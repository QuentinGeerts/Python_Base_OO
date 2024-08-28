# Opérateurs :


## Arithmétiques

# Addition
a = 10
b = 5
somme = a + b
print("La somme est :", somme)  # Affiche: La somme est : 15

# Soustraction
difference = a - b
print("La différence est :", difference)  # Affiche: La différence est : 5

# Multiplication
produit = a * b
print("Le produit est :", produit)  # Affiche: Le produit est : 50

# Division
quotient = a / b
print("Le quotient est :", quotient)  # Affiche: Le quotient est : 2.0

# Division entière
quotient_entier = a // b
print("Le quotient entier est :", quotient_entier)  # Affiche: Le quotient entier est : 2

# Modulo
reste = a % b
print("Le reste est :", reste)  # Affiche: Le reste est : 0

# Exponentiation
puissance = a ** b
print("a élevé à la puissance b est :", puissance)  # Affiche: a élevé à la puissance b est : 100000


## Comparaison

# Opérateurs de comparaison
x = 10
y = 20

# Égalité
print("x == y:", x == y)  # Affiche: False

# Différence
print("x != y:", x != y)  # Affiche: True

# Supérieur
print("x > y:", x > y)   # Affiche: False

# Inférieur
print("x < y:", x < y)   # Affiche: True

# Supérieur ou égal
print("x >= y:", x >= y)  # Affiche: False

# Inférieur ou égal
print("x <= y:", x <= y)  # Affiche: True


## Logique

# Opérateurs logiques

# AND
print("True and True:", True and True)  # Affiche: True
print("False and True:", False and True)  # Affiche: False
print("True and False:", True and False)  # Affiche: False
print("False and False:", False and False)  # Affiche: False

# OR
print("True or True:", True or True)  # Affiche: True
print("False or True:", False or True)  # Affiche: True
print("True or False:", True or False)  # Affiche: True
print("False or False:", False or False)  # Affiche: False

# NOT
print("not True:", not True)    # Affiche: False
print("not False:", not False)    # Affiche: True

# Combinaison d'opérateurs
x = 5
y = 10
z = 15

# Vérifier si x est inférieur à y ET y est inférieur à z
print("(x < y) and (y < z:)", (x < y) and (y < z))  # Affiche: True

# Vérifier si x est supérieur à y OU y est supérieur à z
print("(x > y) or (y > z):", (x > y) or (y > z))   # Affiche: False

# Négation d'une condition
print("not (x < y):", not (x < y))  # Affiche: False
