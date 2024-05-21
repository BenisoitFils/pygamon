class Voiture:
    def __init__(self, modele, annee):
        self.modele = modele
        self.annee = annee

    def afficher_infos(self):
        print(f"Voiture {self.modele} de l'année {self.annee}")

# Création d'une instance de classe
ma_voiture = Voiture("Toyota", 2022)

# Accès aux attributs et appel d'une méthode
print(ma_voiture.modele)  # Affiche "Toyota"
ma_voiture.afficher_infos()  # Affiche "Voiture Toyota de l'année 2022"
print(ma_voiture.annee) # Affiche 2022