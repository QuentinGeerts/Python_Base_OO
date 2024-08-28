from models.GestionPaiement import GestionPaiement

class PaiementCarte(GestionPaiement):
    """Implémentation de l'interface pour les paiements par carte."""

    def __init__(self, titulaire, numero_carte):
        self.titulaire = titulaire
        self.numero_carte = numero_carte
        self.statut = "Non traité"

    def traiter_paiement(self, montant):
        """Implémentation de la méthode pour traiter le paiement par carte."""
        if montant > 0:
            self.statut = "Traitement réussi"
            print(f"Paiement de {montant} euros traité avec la carte.")
        else:
            self.statut = "Échec du traitement"
            print("Montant invalide pour le paiement.")

    def obtenir_statut(self):
        """Implémentation de la méthode pour obtenir le statut du paiement."""
        return self.statut