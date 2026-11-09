class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True
        self.emprunteur = None

    def afficher(self):
        if self.disponible:
            etat = "disponible"
        else:
            etat = "emprunté par " + self.emprunteur
        print(self.titre, "-", self.auteur, "-", self.annee, "-", etat)

    def emprunter(self, nom):
        if not self.disponible:
            print("Ce livre est déjà emprunté.")
            return False
        self.disponible = False
        self.emprunteur = nom
        return True

    def rendre(self):
        if self.disponible:
            print("Ce livre est déjà disponible.")
            return False
        self.disponible = True
        self.emprunteur = None
        return True


class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.emprunts = []

    def emprunter_livre(self, livre):
        if livre.emprunter(self.nom):
            self.emprunts.append(livre)
            return True
        return False

    def rendre_livre(self, livre):
        # Seul l'emprunteur peut rendre le livre.
        if livre not in self.emprunts or livre.emprunteur != self.nom:
            print("Ce livre n'est pas emprunté par cet utilisateur.")
            return False
        if livre.rendre():
            self.emprunts.remove(livre)
            return True
        return False

    def afficher_emprunts(self):
        print("Emprunts de", self.nom)
        if len(self.emprunts) == 0:
            print("Aucun emprunt.")
        for livre in self.emprunts:
            livre.afficher()


if __name__ == "__main__":
    livre = Livre("1984", "Orwell", 1949)
    print(livre.emprunter("Ana"))
    print(livre.emprunter("Léo"))
    print(livre.rendre())
    ana = Utilisateur("Ana")
    ana.emprunter_livre(livre)
    ana.afficher_emprunts()
    ana.rendre_livre(livre)
