# Cette classe représente le plateau du morpion.
class Grille:
    # Le constructeur prépare une nouvelle grille pour chaque partie.
    def __init__(self):
        # Chaque case vide contient un espace. tab contient trois listes de trois cases.
        self.tab = []
        for i in range(3):
            self.tab.append([" ", " ", " "])

    # Afficher les lignes de la grille dans le terminal.
    def afficher(self):
        for i in range(3):
            # join place un séparateur entre les trois cases de la ligne.
            print(" | ".join(self.tab[i]))
            # Il n'y a pas de trait après la dernière ligne.
            if i < 2:
                print("---------")

    # x correspond à la ligne et y à la colonne, numérotées de 0 à 2.
    # True signifie que le coup est accepté, False qu'il est refusé.
    def jouer(self, x, y, joueur):
        # Vérifier les limites avant d'accéder à une case, y compris les indices négatifs.
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Case hors de la grille.")
            return False
        # Seuls les symboles X et O sont autorisés.
        if joueur != "X" and joueur != "O":
            print("Symbole invalide.")
            return False
        # Un symbole déjà présent ne peut pas être remplacé.
        if self.tab[x][y] != " ":
            print("Case déjà occupée.")
            return False

        # Toutes les vérifications sont passées : on inscrit le symbole.
        self.tab[x][y] = joueur
        return True

    # Chercher trois symboles identiques alignés pour le joueur j.
    def est_gagnant(self, j):
        if j != "X" and j != "O":
            return False

        # Vérifier les trois lignes et les trois colonnes.
        for i in range(3):
            if self.tab[i][0] == j and self.tab[i][1] == j and self.tab[i][2] == j:
                return True
            if self.tab[0][i] == j and self.tab[1][i] == j and self.tab[2][i] == j:
                return True

        # Vérifier aussi les deux diagonales.
        if self.tab[0][0] == j and self.tab[1][1] == j and self.tab[2][2] == j:
            return True
        if self.tab[0][2] == j and self.tab[1][1] == j and self.tab[2][0] == j:
            return True
        return False

    # Dès qu'un espace est trouvé, il reste au moins une case libre.
    def est_plein(self):
        for ligne in self.tab:
            if " " in ligne:
                return False
        return True


# Ce jeu d'essai se lance seulement si on exécute directement ce fichier.
if __name__ == "__main__":
    g = Grille()
    g.jouer(0, 0, "X")
    g.jouer(0, 1, "O")
    g.jouer(1, 1, "X")
    g.afficher()
    # Essayer une case occupée puis une case hors de la grille.
    g.jouer(0, 0, "O")
    g.jouer(3, 0, "O")
    print("X a gagné :", g.est_gagnant("X"))
    # Ce dernier coup complète la diagonale de X.
    g.jouer(2, 2, "X")
    print("X a gagné :", g.est_gagnant("X"))
