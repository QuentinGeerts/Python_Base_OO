class CompteBancaire:
    
    def __init__(self, titulaire, solde_initial):
        self.titulaire = titulaire        # Attribut public
        self._solde = solde_initial       # Attribut protégé
        self.__historique = []            # Attribut privé pour stocker l'historique des transactions
    
    def deposer(self, montant):
        """Méthode publique pour déposer de l'argent."""
        if montant > 0:
            self._solde += montant
            self.__ajouter_transaction(f"Dépôt: {montant} euros")
        else:
            print("Montant invalide pour le dépôt.")

    def retirer(self, montant):
        """Méthode publique pour retirer de l'argent."""
        if 0 < montant <= self._solde:
            self._solde -= montant
            self.__ajouter_transaction(f"Retrait: {montant} euros")
        else:
            print("Montant invalide ou insuffisant.")

    def afficher_solde(self):
        """Méthode publique pour afficher le solde."""
        print(f"Le solde de {self.titulaire} est de {self._solde} euros.")

    def _calculer_interet(self):
        """Méthode protégée pour calculer les intérêts (non accessible de l'extérieur)."""
        return self._solde * 0.05

    def appliquer_interet(self):
        """Méthode publique qui utilise une méthode protégée."""
        interet = self._calculer_interet()
        self._solde += interet
        self.__ajouter_transaction(f"Intérêts appliqués: {interet} euros")
        print(f"Intérêts appliqués, nouveau solde: {self._solde} euros.")
    
    def __ajouter_transaction(self, description):
        """Méthode privée pour ajouter une transaction à l'historique."""
        self.__historique.append(description)
    
    def afficher_historique(self):
        """Méthode publique pour afficher l'historique des transactions."""
        print("Historique des transactions :")
        for transaction in self.__historique:
            print(transaction)
