class Grille:
    def __init__(self):
        self.tab = []
        for i in range(3):
            self.tab.append([" ", " ", " "])

    def afficher(self):
        for i in range(3):
            print(" | ".join(self.tab[i]))
            if i < 2:
                print("---------")

    def jouer(self, x, y, joueur):
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Case hors de la grille.")
            return False
        if joueur != "X" and joueur != "O":
            print("Symbole invalide.")
            return False
        if self.tab[x][y] != " ":
            print("Case déjà occupée.")
            return False

        self.tab[x][y] = joueur
        return True

    def est_gagnant(self, j):
        if j != "X" and j != "O":
            return False

        # Vérifier les trois lignes et les trois colonnes.
        for i in range(3):
            if self.tab[i][0] == j and self.tab[i][1] == j and self.tab[i][2] == j:
                return True
            if self.tab[0][i] == j and self.tab[1][i] == j and self.tab[2][i] == j:
                return True

        if self.tab[0][0] == j and self.tab[1][1] == j and self.tab[2][2] == j:
            return True
        if self.tab[0][2] == j and self.tab[1][1] == j and self.tab[2][0] == j:
            return True
        return False

    def est_plein(self):
        for ligne in self.tab:
            if " " in ligne:
                return False
        return True


if __name__ == "__main__":
    g = Grille()
    g.jouer(0, 0, "X")
    g.jouer(0, 1, "O")
    g.jouer(1, 1, "X")
    g.afficher()
    g.jouer(0, 0, "O")
    g.jouer(3, 0, "O")
    print("X a gagné :", g.est_gagnant("X"))
    g.jouer(2, 2, "X")
    print("X a gagné :", g.est_gagnant("X"))
