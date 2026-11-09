# os permet de placer les sauvegardes dans le dossier du programme.
import os

from partie_a import Livre, Utilisateur
# Utiliser la version de Bibliotheque qui possède la sauvegarde CSV.
from partie_c import Bibliotheque


# fichier indique où lire et enregistrer les données de la bibliothèque.
def main(fichier):
    bibliotheque = Bibliotheque()
    # Retrouver les livres, les utilisateurs et les emprunts au lancement.
    bibliotheque.charger(fichier)

    # Réafficher le menu après chaque action jusqu'au choix 6.
    while True:
        print("\n1 Ajouter un livre")
        print("2 Ajouter un utilisateur")
        print("3 Emprunter un livre")
        print("4 Rendre un livre")
        print("5 Afficher les livres")
        print("6 Quitter et sauvegarder")
        # Garder le choix en texte permet aussi de gérer une saisie non numérique.
        choix = input("Ton choix : ").strip()

        # Option 1 : demander les informations pour créer un objet Livre.
        if choix == "1":
            titre = input("Titre : ").strip()
            auteur = input("Auteur : ").strip()
            try:
                annee = int(input("Année : "))  # Convertir le texte en entier.
            except ValueError:
                print("L'année doit être un nombre entier.")
                continue  # Revenir au menu sans ajouter le livre.
            # Refuser les informations obligatoires laissées vides.
            if titre == "" or auteur == "":
                print("Le titre et l'auteur sont obligatoires.")
                continue
            if bibliotheque.ajouter_livre(Livre(titre, auteur, annee)):
                print("Livre ajouté.")

        # Option 2 : créer un utilisateur avec un nom non vide.
        elif choix == "2":
            nom = input("Nom : ").strip()
            if nom == "":
                print("Le nom est obligatoire.")
                continue
            if bibliotheque.ajouter_utilisateur(Utilisateur(nom)):
                print("Utilisateur ajouté.")

        # Option 3 : la bibliothèque vérifie le nom, le titre et la disponibilité.
        elif choix == "3":
            nom = input("Nom de l'utilisateur : ").strip()
            titre = input("Titre du livre : ").strip()
            if bibliotheque.emprunter(nom, titre):
                print("Livre emprunté.")

        # Option 4 : le retour est accepté seulement pour le bon emprunteur.
        elif choix == "4":
            nom = input("Nom de l'utilisateur : ").strip()
            titre = input("Titre du livre : ").strip()
            if bibliotheque.rendre(nom, titre):
                print("Livre rendu.")

        # Option 5 : afficher tous les livres, disponibles comme empruntés.
        elif choix == "5":
            bibliotheque.afficher_livres()

        # Option 6 : quitter seulement si la sauvegarde a réussi.
        elif choix == "6":
            if bibliotheque.sauvegarder(fichier):
                print("Données sauvegardées. Au revoir !")
                break  # Sortir de la boucle du menu.

        # Tout autre choix affiche un message puis le menu revient.
        else:
            print("Choix invalide.")


# Ce bloc lance le menu uniquement à l'exécution directe de ce fichier.
if __name__ == "__main__":
    # Garder la sauvegarde dans TP3, quel que soit le dossier de lancement.
    fichier = os.path.join(os.path.dirname(__file__), "bibliotheque.csv")
    main(fichier)
