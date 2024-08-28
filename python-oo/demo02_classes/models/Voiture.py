class Voiture:
    # Constructeur
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    # Méthode d'instance
    def afficher_details(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}")