# Gestion des erreurs

try:
    # Code susceptible de générer plusieurs types d'erreurs
    nombre = int(input("Entrez un nombre : "))
    resultat = 10 / nombre
except ValueError:
    # Exception pour une entrée invalide qui ne peut être convertie en nombre
    print("Erreur : vous devez entrer un nombre.")
except ZeroDivisionError:
    # Exception pour la division par zéro
    print("Erreur : division par zéro.")
except Exception as e:
    # Gestion générique de toute autre exception
    print(f"Erreur inattendue : {e}")
else:
    # Code qui s'exécute si aucune exception n'est levée
    print(f"Résultat de la division : {resultat}")
finally:
    # Code qui s'exécute toujours
    print("Fin de l'opération.")


# Lever une exception manuellement

def verifier_age(age):
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif.")
    else:
        print(f"L'âge est {age}.")

try:
    verifier_age(-5)
except ValueError as e:
    print(f"Erreur capturée : {e}")
