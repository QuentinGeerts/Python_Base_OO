# Encapsulation

from models.CompteBancaire import CompteBancaire

# public    : 
# → Accessible partout
# protected : _
# → Accessible partout mais destiné à un usage interne
# private   : __
# → Accessible uniquement dans la classe

# Création d'une instance de CompteBancaire
compte = CompteBancaire("Alice", 1000)

# Effectuer des transactions
compte.deposer(500)
compte.retirer(200)
compte.appliquer_interet()

# Afficher le solde et l'historique des transactions
compte.afficher_solde()
print('Solde du compte', compte._solde)
compte.afficher_historique()

# Tentatives d'accès aux attributs et méthodes privés
# print(compte.__historique)  # Provoque une erreur d'attribut
# compte.__ajouter_transaction("Test")  # Provoque une erreur d'attribut


"""" Sortie attendue :
Le solde de Alice est de 1365.0 euros.
Historique des transactions :
Dépôt: 500 euros
Retrait: 200 euros
Intérêts appliqués: 65.0 euros
"""