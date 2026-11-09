# Un objet Livre contient les informations d'un livre et son état d'emprunt.
class Livre:
    def __init__(self, titre, auteur, annee):
        # self désigne l'objet sur lequel on travaille.
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        # Un nouveau livre est disponible et n'a pas encore d'emprunteur.
        self.disponible = True
        self.emprunteur = None

    # Afficher les informations du livre et préciser s'il peut être emprunté.
    def afficher(self):
        if self.disponible:
            etat = "disponible"
        else:
            etat = "emprunté par " + self.emprunteur
        print(self.titre, "-", self.auteur, "-", self.annee, "-", etat)

    # Renvoyer True si l'emprunt réussit, False si le livre est déjà pris.
    def emprunter(self, nom):
        if not self.disponible:
            print("Ce livre est déjà emprunté.")
            return False
        # Retenir le nom de la personne pour savoir qui doit rendre le livre.
        self.disponible = False
        self.emprunteur = nom
        return True

    # Remettre le livre à disposition après un emprunt.
    def rendre(self):
        if self.disponible:
            print("Ce livre est déjà disponible.")
            return False
        self.disponible = True
        self.emprunteur = None  # None signifie qu'il n'y a plus d'emprunteur.
        return True


# Un utilisateur possède un nom et une liste de livres empruntés.
class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.emprunts = []  # La liste contient des objets Livre, pas des titres.

    # Ajouter le livre à la liste seulement si son emprunt est accepté.
    def emprunter_livre(self, livre):
        if livre.emprunter(self.nom):
            self.emprunts.append(livre)
            return True
        return False

    # Vérifier le propriétaire de l'emprunt avant de rendre le livre.
    def rendre_livre(self, livre):
        # Seul l'emprunteur peut rendre le livre.
        if livre not in self.emprunts or livre.emprunteur != self.nom:
            print("Ce livre n'est pas emprunté par cet utilisateur.")
            return False
        # Mettre à jour le livre puis la liste de l'utilisateur.
        if livre.rendre():
            self.emprunts.remove(livre)
            return True
        return False

    # Réutiliser afficher() pour présenter chaque livre de l'utilisateur.
    def afficher_emprunts(self):
        print("Emprunts de", self.nom)
        if len(self.emprunts) == 0:
            print("Aucun emprunt.")
        for livre in self.emprunts:
            livre.afficher()


# Exemples exécutés uniquement quand on lance ce fichier directement.
if __name__ == "__main__":
    livre = Livre("1984", "Orwell", 1949)
    print(livre.emprunter("Ana"))
    print(livre.emprunter("Léo"))
    print(livre.rendre())
    # Essayer ensuite l'emprunt et le retour à travers un utilisateur.
    ana = Utilisateur("Ana")
    ana.emprunter_livre(livre)
    ana.afficher_emprunts()
    ana.rendre_livre(livre)
