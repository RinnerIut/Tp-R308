# Réutiliser les classes créées dans les deux premières parties.
from partie_a import Grille
from partie_b import JoueurHumain, JoueurIA


# Les joueurs peuvent être humains ou IA, car ils ont tous prochain_coup().
def jouer_partie(joueur_x, joueur_o):
    # Chaque partie commence avec une grille vide et le joueur X.
    grille = Grille()
    symbole = "X"

    # Répéter les tours jusqu'à une victoire ou un match nul.
    while True:
        grille.afficher()
        # Sélectionner l'objet joueur correspondant au symbole du tour.
        if symbole == "X":
            joueur = joueur_x
        else:
            joueur = joueur_o

        # Récupérer les deux coordonnées proposées par le joueur.
        x, y = joueur.prochain_coup(grille.tab, symbole)
        # La grille vérifie le coup avant de poser le symbole.
        if not grille.jouer(x, y, symbole):
            continue  # Le même joueur rejoue si le coup est refusé.

        # Tester la victoire avant le match nul : le dernier coup peut être gagnant.
        if grille.est_gagnant(symbole):
            grille.afficher()
            print("Le joueur", symbole, "a gagné !")
            return symbole  # Quitter la fonction et indiquer le gagnant.

        # Sans gagnant ni case libre, la partie est un match nul.
        if grille.est_plein():
            grille.afficher()
            print("Match nul !")
            return "nul"

        # Après un coup valide sans fin de partie, passer à l'autre joueur.
        if symbole == "X":
            symbole = "O"
        else:
            symbole = "X"


# Lancer une partie humain contre ordinateur à l'exécution du fichier.
if __name__ == "__main__":
    print("Morpion : tu joues X, l'ordinateur joue O.")
    jouer_partie(JoueurHumain(), JoueurIA())
