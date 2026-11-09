# Importer les classes de base pour ne pas réécrire leur code.
from partie_a import Livre, Utilisateur


# Cette classe regroupe les livres et les utilisateurs.
class Bibliotheque:
    def __init__(self):
        # Les clés sont les titres des livres et les noms des utilisateurs.
        # Les valeurs sont les objets Livre et Utilisateur correspondants.
        self.livres = {}
        self.utilisateurs = {}

    # Chaque titre doit être unique pour ne pas remplacer un livre existant.
    def ajouter_livre(self, livre):
        if livre.titre in self.livres:
            print("Ce titre existe déjà.")
            return False
        # Enregistrer l'objet dans le dictionnaire avec son titre comme clé.
        self.livres[livre.titre] = livre
        return True

    # Refuser les noms déjà présents pour conserver les emprunts existants.
    def ajouter_utilisateur(self, utilisateur):
        if utilisateur.nom in self.utilisateurs:
            print("Cet utilisateur existe déjà.")
            return False
        self.utilisateurs[utilisateur.nom] = utilisateur
        return True

    # Chercher les objets à partir du nom et du titre fournis.
    def emprunter(self, nom, titre):
        # Vérifier les clés avant l'accès pour éviter une erreur KeyError.
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu.")
            return False
        if titre not in self.livres:
            print("Livre inconnu.")
            return False
        # L'utilisateur gère l'emprunt et la mise à jour de sa liste.
        return self.utilisateurs[nom].emprunter_livre(self.livres[titre])

    # Les mêmes vérifications sont nécessaires pour un retour.
    def rendre(self, nom, titre):
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu.")
            return False
        if titre not in self.livres:
            print("Livre inconnu.")
            return False
        # rendre_livre vérifie aussi que cet utilisateur est bien l'emprunteur.
        return self.utilisateurs[nom].rendre_livre(self.livres[titre])

    # Afficher le catalogue avec l'état disponible ou emprunté de chaque livre.
    def afficher_livres(self):
        if len(self.livres) == 0:
            print("Aucun livre dans la bibliothèque.")
        # values() permet de parcourir les objets plutôt que leurs titres.
        for livre in self.livres.values():
            livre.afficher()


# Exemple : créer une bibliothèque, emprunter un livre puis le rendre.
if __name__ == "__main__":
    b = Bibliotheque()
    b.ajouter_livre(Livre("1984", "Orwell", 1949))
    b.ajouter_utilisateur(Utilisateur("Ana"))
    b.emprunter("Ana", "1984")
    b.afficher_livres()
    b.rendre("Ana", "1984")
    b.afficher_livres()
