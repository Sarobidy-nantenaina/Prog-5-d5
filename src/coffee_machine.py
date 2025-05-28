import random

class Boisson:
    """Représente une boisson disponible dans la machine."""
    def __init__(self, nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock

    def est_disponible(self):
        return self.stock > 0

    def retirer_stock(self):
        if self.stock > 0:
            self.stock -= 1

class Ressources:
    """Gère les ressources de la machine."""
    def __init__(self, eau=5, dosettes=5, gobelets=5):
        self.eau = eau
        self.dosettes = dosettes
        self.gobelets = gobelets

    def verifier(self):
        if self.eau <= 0:
            print("Réservoir d'eau vide.")
            return False
        if self.dosettes <= 0:
            print("Aucune dosette détectée.")
            return False
        if self.gobelets <= 0:
            print("Aucun gobelet détecté.")
            return False
        return True

    def consommer(self):
        self.eau -= 1
        self.dosettes -= 1
        self.gobelets -= 1

class Paiement:
    """Gère le paiement."""
    @staticmethod
    def demander(prix):
        print("\nMéthodes de paiement :")
        print("1. Carte bancaire")
        print("2. Mobile Money")
        choix = input("Choisissez votre méthode de paiement (1/2) : ")
        if choix not in ('1', '2'):
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

class CoffeeMachine:
    """Gère le fonctionnement de la machine à café."""
    def __init__(self):
        self.boissons = [
            Boisson("Espresso", 1.5, 5),
            Boisson("Latte", 2.0, 3),
            Boisson("Thé", 1.0, 2)
        ]
        self.ressources = Ressources()
        self.en_marche = True

    def afficher_menu(self):
        print("\nMenu des boissons :")
        for idx, boisson in enumerate(self.boissons, 1):
            print(f"{idx}. {boisson.nom} - {boisson.prix:.2f}€ (stock: {boisson.stock})")

    def choisir_boisson(self):
        self.afficher_menu()
        choix = input("Sélectionnez une boisson (numéro) : ")
        if not choix.isdigit():
            print("Choix invalide.")
            return None
        idx = int(choix) - 1
        if not (0 <= idx < len(self.boissons)):
            print("Choix invalide.")
            return None
        boisson = self.boissons[idx]
        if not boisson.est_disponible():
            print("Boisson en rupture de stock.")
            return None
        return boisson

    def verifier_machine(self):
        if not self.en_marche or random.random() < 0.05:
            print("Erreur interne (température/pression/panne).")
            return False
        return True

    def distribuer_boisson(self, boisson):
        print(f"Préparation de votre {boisson.nom}...")
        boisson.retirer_stock()
        self.ressources.consommer()
        print("Votre boisson est prête. Bonne dégustation !")

    def demander_reessai(self):
        reponse = input("Voulez-vous réessayer ? (o/n) : ")
        return reponse.strip().lower() == 'o'

    def demander_autre_boisson(self):
        reponse = input("Voulez-vous une autre boisson ? (o/n) : ")
        return reponse.strip().lower() == 'o'

    def run(self):
        print("Bienvenue sur la machine à café !")
        while True:
            boisson = self.choisir_boisson()
            if not boisson:
                if not self.demander_reessai():
                    print("Merci et à bientôt !")
                    break
                continue

            if not self.ressources.verifier():
                if not self.demander_reessai():
                    print("Merci et à bientôt !")
                    break
                continue

            if not self.verifier_machine():
                if not self.demander_reessai():
                    print("Merci et à bientôt !")
                    break
                continue

            if not Paiement.demander(boisson.prix):
                if not self.demander_reessai():
                    print("Merci et à bientôt !")
                    break
                continue

            self.distribuer_boisson(boisson)

            if not self.demander_autre_boisson():
                print("Merci et à bientôt !")
                break

if __name__ == "__main__":
    CoffeeMachine().run()