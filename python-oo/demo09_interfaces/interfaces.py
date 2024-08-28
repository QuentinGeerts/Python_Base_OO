from models.PaiementCarte import PaiementCarte
from models.PaiementPaypal import PaiementPayPal

# Création d'instances des classes concrètes
paiement_carte = PaiementCarte("Jean Dupont", "1234 5678 9012 3456")
paiement_paypal = PaiementPayPal("jean.dupont@example.com")

# Traitement des paiements
paiement_carte.traiter_paiement(100)  # Affiche: Paiement de 100 euros traité avec la carte.
paiement_paypal.traiter_paiement(50)  # Affiche: Paiement de 50 euros traité via PayPal.

# Obtention des statuts
print(paiement_carte.obtenir_statut())  # Affiche: Traitement réussi
print(paiement_paypal.obtenir_statut()) # Affiche: Traitement réussi