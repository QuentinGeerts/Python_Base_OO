from abc import ABC, abstractmethod

class GestionPaiement(ABC):
    """Interface pour la gestion des paiements."""

    @abstractmethod
    def traiter_paiement(self, montant):
        """Méthode abstraite pour traiter un paiement."""
        pass

    @abstractmethod
    def obtenir_statut(self):
        """Méthode abstraite pour obtenir le statut du paiement."""
        pass