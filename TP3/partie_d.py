import os

from partie_a import Livre, Utilisateur
from partie_c import Bibliotheque


def main(fichier):
    bibliotheque = Bibliotheque()
    bibliotheque.charger(fichier)

    while True:
        print("\n1 Ajouter un livre")
        print("2 Ajouter un utilisateur")
        print("3 Emprunter un livre")
        print("4 Rendre un livre")
        print("5 Afficher les livres")
        print("6 Quitter et sauvegarder")
        choix = input("Ton choix : ").strip()

        if choix == "1":
            titre = input("Titre : ").strip()
            auteur = input("Auteur : ").strip()
            try:
                annee = int(input("Année : "))
            except ValueError:
                print("L'année doit être un nombre entier.")
                continue
            if titre == "" or auteur == "":
                print("Le titre et l'auteur sont obligatoires.")
                continue
            if bibliotheque.ajouter_livre(Livre(titre, auteur, annee)):
                print("Livre ajouté.")

        elif choix == "2":
            nom = input("Nom : ").strip()
            if nom == "":
                print("Le nom est obligatoire.")
                continue
            if bibliotheque.ajouter_utilisateur(Utilisateur(nom)):
                print("Utilisateur ajouté.")

        elif choix == "3":
            nom = input("Nom de l'utilisateur : ").strip()
            titre = input("Titre du livre : ").strip()
            if bibliotheque.emprunter(nom, titre):
                print("Livre emprunté.")

        elif choix == "4":
            nom = input("Nom de l'utilisateur : ").strip()
            titre = input("Titre du livre : ").strip()
            if bibliotheque.rendre(nom, titre):
                print("Livre rendu.")

        elif choix == "5":
            bibliotheque.afficher_livres()

        elif choix == "6":
            if bibliotheque.sauvegarder(fichier):
                print("Données sauvegardées. Au revoir !")
                break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    # Garder la sauvegarde dans TP3, quel que soit le dossier de lancement.
    fichier = os.path.join(os.path.dirname(__file__), "bibliotheque.csv")
    main(fichier)
