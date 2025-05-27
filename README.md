# ☕ Projet : Machine à Café (Coffee Machine)

Ce projet consiste à développer un programme simulant le fonctionnement d’une machine à café, destiné à être intégré ultérieurement dans un système ou une machine réelle. Il permet à un utilisateur de choisir une boisson, d’insérer de l’argent et de recevoir sa boisson. Le projet est actuellement en cours de développement.

---

## 🎯 Objectif

- Simuler une machine à café virtuelle.
- Mettre en pratique la programmation orientée objet.
- Gérer les cas d’utilisation et les erreurs fréquentes.
- Créer une base solide pour une future interface graphique ou physique.

---

## 🧑‍💻 Cas d'utilisation (Use Case)

1. L'utilisateur démarre la machine.
2. Un menu de boissons est affiché avec les prix.
3. L'utilisateur sélectionne une boisson.
4. La machine demande l’argent nécessaire.
5. Si le montant est suffisant, la boisson est préparée.
6. Si le montant est insuffisant, un message d’erreur est affiché.
7. La machine peut gérer plusieurs commandes successives.

---

## ❌ Gestion des erreurs prévue

- Boisson en rupture de stock
- Réservoir d’eau vide
- Bac à déchets plein
- Montant d’argent insuffisant
- Choix invalide de boisson

---

## 🧱 Modélisation prévue

### Entités principales

- `CoffeeMachine` : contrôle général (état, menu, paiement)
- `Boisson` : nom, prix, stock
- `EtatMachine` : énumération des états possibles (`ETEINT`, `EN_FONCTION`, `MAINTENANCE`, etc.)

---

## 📁 Structure du projet (prévisionnelle)

```plaintext
coffee-machine/
├── src/
│   ├── Main
│   ├── CoffeeMachine
│   ├── Boisson
│   └── EtatMachine
├── tests/
├── README.md
