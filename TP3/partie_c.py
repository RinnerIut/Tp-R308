# csv lit et écrit les tableaux de données ; os sert à construire les chemins.
import csv
import os

from partie_a import Livre, Utilisateur
# Renommer la classe importée pour la distinguer de celle créée ci-dessous.
from partie_b import Bibliotheque as BibliothequeBase


# L'héritage permet de garder les méthodes de la partie B et d'en ajouter deux.
class Bibliotheque(BibliothequeBase):
    # Enregistrer les livres et les utilisateurs dans deux fichiers CSV.
    def sauvegarder(self, fichier):
        # Retirer l'extension pour construire le nom du fichier des utilisateurs.
        fichier_utilisateurs = os.path.splitext(fichier)[0] + "_utilisateurs.csv"
        try:
            # Le mode w remplace l'ancienne sauvegarde. with ferme le fichier.
            # UTF-8 conserve les accents et newline évite les lignes vides sous Windows.
            with open(fichier, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                # La première ligne donne le nom des colonnes.
                writer.writerow(["titre", "auteur", "annee", "disponible", "emprunteur"])
                # Chaque ligne suivante décrit un livre et son emprunt éventuel.
                for livre in self.livres.values():
                    writer.writerow([livre.titre, livre.auteur, livre.annee,
                                     livre.disponible, livre.emprunteur])

            # Conserver aussi les utilisateurs qui n'ont aucun emprunt.
            with open(fichier_utilisateurs, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["nom"])
                for nom in self.utilisateurs:
                    writer.writerow([nom])
        # Par exemple, l'écriture peut échouer si le dossier n'est pas accessible.
        except OSError:
            print("Impossible de sauvegarder les données.")
            return False
        return True

    # Reconstruire les objets Python à partir des données enregistrées.
    def charger(self, fichier):
        fichier_utilisateurs = os.path.splitext(fichier)[0] + "_utilisateurs.csv"
        try:
            with open(fichier, "r", newline="", encoding="utf-8") as f:
                # DictReader utilise les noms de colonnes comme clés de dictionnaire.
                lignes = list(csv.DictReader(f))
        except FileNotFoundError:
            # Au premier lancement, il est normal de ne pas avoir de fichier.
            print("Aucune sauvegarde : la bibliothèque démarre vide.")
            return False
        except (OSError, UnicodeError, csv.Error):
            print("Impossible de lire la sauvegarde.")
            return False

        # Remplacer les anciennes données uniquement après avoir lu le fichier.
        self.livres = {}
        self.utilisateurs = {}
        try:
            with open(fichier_utilisateurs, "r", newline="", encoding="utf-8") as f:
                for ligne in csv.DictReader(f):
                    # strip retire les espaces inutiles autour du nom.
                    nom = ligne["nom"].strip()
                    if nom != "":
                        self.utilisateurs[nom] = Utilisateur(nom)
        except FileNotFoundError:
            pass  # Les emprunteurs seront recréés à partir des livres.
        except (OSError, UnicodeError, csv.Error, KeyError, AttributeError):
            print("Impossible de lire la liste des utilisateurs.")

        # Lire les informations de chaque livre et vérifier leur format.
        for ligne in lignes:
            try:
                titre = ligne["titre"]
                auteur = ligne["auteur"]
                annee = int(ligne["annee"])  # Le CSV contient du texte.
                disponible = ligne["disponible"]
                nom = ligne["emprunteur"]
                if not titre or not auteur or disponible not in ("True", "False"):
                    raise ValueError
                # Un livre emprunté doit obligatoirement avoir un emprunteur.
                if disponible == "False" and not nom:
                    raise ValueError
            except (KeyError, ValueError, TypeError):
                print("Ligne de sauvegarde incorrecte ignorée.")
                continue  # Passer à la ligne suivante si celle-ci est incorrecte.

            # Le constructeur crée d'abord un livre disponible.
            livre = Livre(titre, auteur, annee)
            # Si nécessaire, rétablir l'emprunt dans le livre et chez l'utilisateur.
            if self.ajouter_livre(livre) and disponible == "False":
                if nom not in self.utilisateurs:
                    self.ajouter_utilisateur(Utilisateur(nom))
                self.emprunter(nom, titre)
        return True


# Démonstration dans des fichiers séparés de ceux du menu de la partie D.
if __name__ == "__main__":
    fichier = os.path.join(os.path.dirname(__file__), "exemple_bibliotheque.csv")
    b = Bibliotheque()
    b.ajouter_livre(Livre("1984", "Orwell", 1949))
    b.ajouter_utilisateur(Utilisateur("Ana"))
    b.emprunter("Ana", "1984")
    if b.sauvegarder(fichier):
        # Une nouvelle bibliothèque permet de vérifier que le CSV suffit à tout relire.
        nouvelle = Bibliotheque()
        nouvelle.charger(fichier)
        nouvelle.afficher_livres()
        nouvelle.rendre("Ana", "1984")
        nouvelle.afficher_livres()
