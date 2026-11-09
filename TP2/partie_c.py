from partie_a import Grille
from partie_b import JoueurHumain, JoueurIA


def jouer_partie(joueur_x, joueur_o):
    grille = Grille()
    symbole = "X"

    while True:
        grille.afficher()
        if symbole == "X":
            joueur = joueur_x
        else:
            joueur = joueur_o

        x, y = joueur.prochain_coup(grille.tab, symbole)
        if not grille.jouer(x, y, symbole):
            continue  # Le même joueur rejoue si le coup est refusé.

        if grille.est_gagnant(symbole):
            grille.afficher()
            print("Le joueur", symbole, "a gagné !")
            return symbole

        if grille.est_plein():
            grille.afficher()
            print("Match nul !")
            return "nul"

        if symbole == "X":
            symbole = "O"
        else:
            symbole = "X"


if __name__ == "__main__":
    print("Morpion : tu joues X, l'ordinateur joue O.")
    jouer_partie(JoueurHumain(), JoueurIA())
