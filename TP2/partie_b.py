import random


class JoueurHumain:
    def prochain_coup(self, tab, symbole):
        while True:
            try:
                print("Joueur", symbole)
                x = int(input("Ligne (0 à 2) : "))
                y = int(input("Colonne (0 à 2) : "))
                return (x, y)
            except ValueError:
                print("Entre des nombres entiers.")


class JoueurIA:
    def prochain_coup(self, tab, symbole):
        cases_libres = []
        for x in range(3):
            for y in range(3):
                if tab[x][y] == " ":
                    cases_libres.append((x, y))

        if len(cases_libres) == 0:
            return None
        return random.choice(cases_libres)


if __name__ == "__main__":
    from partie_a import Grille

    grille = Grille()
    ia = JoueurIA()
    print("Coup de l'IA :", ia.prochain_coup(grille.tab, "O"))
    humain = JoueurHumain()
    print("Coup du joueur :", humain.prochain_coup(grille.tab, "X"))
