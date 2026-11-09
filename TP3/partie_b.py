from partie_a import Livre, Utilisateur


class Bibliotheque:
    def __init__(self):
        self.livres = {}
        self.utilisateurs = {}

    def ajouter_livre(self, livre):
        if livre.titre in self.livres:
            print("Ce titre existe déjà.")
            return False
        self.livres[livre.titre] = livre
        return True

    def ajouter_utilisateur(self, utilisateur):
        if utilisateur.nom in self.utilisateurs:
            print("Cet utilisateur existe déjà.")
            return False
        self.utilisateurs[utilisateur.nom] = utilisateur
        return True

    def emprunter(self, nom, titre):
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu.")
            return False
        if titre not in self.livres:
            print("Livre inconnu.")
            return False
        return self.utilisateurs[nom].emprunter_livre(self.livres[titre])

    def rendre(self, nom, titre):
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu.")
            return False
        if titre not in self.livres:
            print("Livre inconnu.")
            return False
        return self.utilisateurs[nom].rendre_livre(self.livres[titre])

    def afficher_livres(self):
        if len(self.livres) == 0:
            print("Aucun livre dans la bibliothèque.")
        for livre in self.livres.values():
            livre.afficher()


if __name__ == "__main__":
    b = Bibliotheque()
    b.ajouter_livre(Livre("1984", "Orwell", 1949))
    b.ajouter_utilisateur(Utilisateur("Ana"))
    b.emprunter("Ana", "1984")
    b.afficher_livres()
    b.rendre("Ana", "1984")
    b.afficher_livres()
