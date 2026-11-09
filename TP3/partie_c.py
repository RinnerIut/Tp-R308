import csv
import os

from partie_a import Livre, Utilisateur
from partie_b import Bibliotheque as BibliothequeBase


# Ajouter la sauvegarde à la bibliothèque de la partie B.
class Bibliotheque(BibliothequeBase):
    def sauvegarder(self, fichier):
        fichier_utilisateurs = os.path.splitext(fichier)[0] + "_utilisateurs.csv"
        try:
            with open(fichier, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["titre", "auteur", "annee", "disponible", "emprunteur"])
                for livre in self.livres.values():
                    writer.writerow([livre.titre, livre.auteur, livre.annee,
                                     livre.disponible, livre.emprunteur])

            # Conserver aussi les utilisateurs qui n'ont aucun emprunt.
            with open(fichier_utilisateurs, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["nom"])
                for nom in self.utilisateurs:
                    writer.writerow([nom])
        except OSError:
            print("Impossible de sauvegarder les données.")
            return False
        return True

    def charger(self, fichier):
        fichier_utilisateurs = os.path.splitext(fichier)[0] + "_utilisateurs.csv"
        try:
            with open(fichier, "r", newline="", encoding="utf-8") as f:
                lignes = list(csv.DictReader(f))
        except FileNotFoundError:
            print("Aucune sauvegarde : la bibliothèque démarre vide.")
            return False
        except (OSError, UnicodeError, csv.Error):
            print("Impossible de lire la sauvegarde.")
            return False

        self.livres = {}
        self.utilisateurs = {}
        try:
            with open(fichier_utilisateurs, "r", newline="", encoding="utf-8") as f:
                for ligne in csv.DictReader(f):
                    nom = ligne["nom"].strip()
                    if nom != "":
                        self.utilisateurs[nom] = Utilisateur(nom)
        except FileNotFoundError:
            pass  # Les emprunteurs seront recréés à partir des livres.
        except (OSError, UnicodeError, csv.Error, KeyError, AttributeError):
            print("Impossible de lire la liste des utilisateurs.")

        for ligne in lignes:
            try:
                titre = ligne["titre"]
                auteur = ligne["auteur"]
                annee = int(ligne["annee"])
                disponible = ligne["disponible"]
                nom = ligne["emprunteur"]
                if not titre or not auteur or disponible not in ("True", "False"):
                    raise ValueError
                if disponible == "False" and not nom:
                    raise ValueError
            except (KeyError, ValueError, TypeError):
                print("Ligne de sauvegarde incorrecte ignorée.")
                continue

            livre = Livre(titre, auteur, annee)
            if self.ajouter_livre(livre) and disponible == "False":
                if nom not in self.utilisateurs:
                    self.ajouter_utilisateur(Utilisateur(nom))
                self.emprunter(nom, titre)
        return True


if __name__ == "__main__":
    fichier = os.path.join(os.path.dirname(__file__), "exemple_bibliotheque.csv")
    b = Bibliotheque()
    b.ajouter_livre(Livre("1984", "Orwell", 1949))
    b.ajouter_utilisateur(Utilisateur("Ana"))
    b.emprunter("Ana", "1984")
    if b.sauvegarder(fichier):
        nouvelle = Bibliotheque()
        nouvelle.charger(fichier)
        nouvelle.afficher_livres()
        nouvelle.rendre("Ana", "1984")
        nouvelle.afficher_livres()
