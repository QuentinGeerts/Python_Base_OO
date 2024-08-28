# Structures itératives

# 1. La boucle "for"

"""
for variable in séquence:
    # Bloc de code à exécuter pour chaque élément de la séquence
"""

fruits = ["pomme", "banane", "cerise"]

for fruit in fruits:
    print(fruit)
    

message = "Bonjour"

for lettre in message:
    print(lettre)

# Boucle "for" avec "enumerate()"

for i, fruit in enumerate(fruits):
    print("Index:", i)
    print("Fruit:", fruit)

# Boucle "for" avec "range()"

for i in range(5):
    print(i)

for i in range(0, 6, 2):
    print(i)

# 2. La boucle while

"""
while condition:
    # Bloc de code à exécuter tant que la condition est vraie
"""

compteur = 0

while compteur < 5:
    print(compteur)
    compteur += 1


# Boucle while avec condition d'arrêt

reponse = ""

while reponse.lower() != "oui":
    reponse = input("Voulez-vous continuer ? (oui/non) ")
    if reponse.lower() == "oui":
        print("Vous avez choisi de continuer.")
    else:
        print("Vous avez choisi de ne pas continuer.")

# 3. Instructions break et continue

# Exemple avec "break"
for i in range(10):
    if i == 5:
        break # La boucle s'arrête lorsque i atteint 5
    print(i)

# Exemple avec "continue"
for i in range(10):
    if i % 2 == 0:
        continue # L'instruction continue ignore les nombres pairs et passe directement à l'itération suivante.
    print(i)

# 4. Boucle imbriquée

for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
