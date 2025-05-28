import random

class Boisson:
    """Classe représentant une boisson."""
    def __init__(self, nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock

class CoffeeMachine:
    """Classe représentant la machine à café."""
    def __init__(self):
        self.boissons = [
            Boisson("Espresso", 1.5, 5),
            Boisson("Latte", 2.0, 3),
            Boisson("Thé", 1.0, 2)
        ]
        self.eau = 5
        self.pods = 5
        self.cups = 5
        self.en_marche = True

    def afficher_menu(self):
        print("\nMenu des boissons :")
        for idx, boisson in enumerate(self.boissons, 1):
            print(f"{idx}. {boisson.nom} - {boisson.prix:.2f}€ (stock: {boisson.stock})")

    def paiement(self, prix):
        print("\nMéthodes de paiement :")
        print("1. Carte bancaire")
        print("2. Mobile Money")
        choix = input("Choisissez votre méthode de paiement (1/2) : ")
        if choix not in ['1', '2']:
            print("Méthode invalide.")
            return False
        try:
            montant = float(input(f"Veuillez entrer {prix:.2f}€ : "))
        except ValueError:
            print("Montant invalide.")
            return False
        if montant < prix:
            print("Fonds insuffisants.")
            return False
        if random.random() < 0.1:
            print("Échec du paiement (connexion ou refus).")
            return False
        print("Paiement accepté.")
        if montant > prix:
            rendu = montant - prix
            print(f"Rendu de monnaie : {rendu:.2f}€")
        return True

    def choisir_boisson(self):
        self.afficher_menu()
        choix = input("Sélectionnez une boisson (numéro) : ")
        if not choix.isdigit() or int(choix) not in range(1, len(self.boissons)+1):
            print("Choix invalide.")
            return None
        boisson = self.boissons[int(choix)-1]
        if boisson.stock <= 0:
            print("Boisson en rupture de stock.")
            return None
        if self.pods <= 0:
            print("Aucune dosette détectée.")
            return None
        if self.eau <= 0:
            print("Réservoir d'eau vide.")
            return None
        if not self.en_marche or random.random() < 0.05:
            print("Erreur interne (température/pression/panne).")
            return None
        return boisson

    def distribuer(self, boisson):
        if self.cups <= 0:
            print("Aucun gobelet détecté. Distribution annulée.")
            return False
        print(f"Préparation de votre {boisson.nom}...")
        boisson.stock -= 1
        self.eau -= 1
        self.pods -= 1
        self.cups -= 1
        print("Votre boisson est prête. Bonne dégustation !")
        return True

    def run(self):
        print("Bienvenue sur la machine à café !")
        while True:
            boisson = self.choisir_boisson()
            if not boisson:
                continuer = input("Voulez-vous réessayer ? (o/n) : ")
                if continuer.lower() != 'o':
                    print("Merci et à bientôt !")
                    break
                continue
            if not self.paiement(boisson.prix):
                continuer = input("Voulez-vous réessayer ? (o/n) : ")
                if continuer.lower() != 'o':
                    print("Merci et à bientôt !")
                    break
                continue
            if not self.distribuer(boisson):
                continuer = input("Voulez-vous réessayer ? (o/n) : ")
                if continuer.lower() != 'o':
                    print("Merci et à bientôt !")
                    break
                continue
            encore = input("Voulez-vous une autre boisson ? (o/n) : ")
            if encore.lower() != 'o':
                print("Merci et à bientôt !")
                break

if __name__ == "__main__":
    CoffeeMachine().run()