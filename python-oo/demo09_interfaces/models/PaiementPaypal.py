from models.GestionPaiement import GestionPaiement

class PaiementPayPal(GestionPaiement):
    """Implémentation de l'interface pour les paiements via PayPal."""

    def __init__(self, compte_email):
        self.compte_email = compte_email
        self.statut = "Non traité"

    def traiter_paiement(self, montant):
        """Implémentation de la méthode pour traiter le paiement PayPal."""
        if montant > 0:
            self.statut = "Traitement réussi"
            print(f"Paiement de {montant} euros traité via PayPal.")
        else:
            self.statut = "Échec du traitement"
            print("Montant invalide pour le paiement.")

    def obtenir_statut(self):
        """Implémentation de la méthode pour obtenir le statut du paiement."""
        return self.statut