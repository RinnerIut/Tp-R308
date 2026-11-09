# random permet à l'ordinateur de choisir une case au hasard.
import random


# Le joueur humain choisit son coup au clavier.
class JoueurHumain:
    # Les deux classes utilisent la même méthode pour être utilisées par le jeu.
    # tab est la grille et symbole est la lettre du joueur (X ou O).
    def prochain_coup(self, tab, symbole):
        # Redemander la saisie tant qu'elle ne contient pas des entiers.
        while True:
            try:
                print("Joueur", symbole)
                # input renvoie du texte : int le convertit en nombre entier.
                x = int(input("Ligne (0 à 2) : "))
                y = int(input("Colonne (0 à 2) : "))
                # Le jeu vérifiera ensuite les limites et si la case est libre.
                return (x, y)
            except ValueError:
                # Une lettre à la place d'un nombre ne doit pas arrêter le jeu.
                print("Entre des nombres entiers.")


# L'ordinateur choisit uniquement parmi les cases encore libres.
class JoueurIA:
    def prochain_coup(self, tab, symbole):
        cases_libres = []
        # Parcourir toutes les lignes puis toutes les colonnes.
        for x in range(3):
            for y in range(3):
                if tab[x][y] == " ":
                    # Mémoriser les coordonnées de chaque case vide.
                    cases_libres.append((x, y))

        # Éviter de tirer au hasard dans une liste vide.
        if len(cases_libres) == 0:
            return None
        # choice renvoie un des couples (ligne, colonne) de la liste.
        return random.choice(cases_libres)


# Essayer les deux joueurs sans lancer une partie complète.
# Ce bloc ne se lance pas lors de l'import dans la partie C.
if __name__ == "__main__":
    from partie_a import Grille

    grille = Grille()
    ia = JoueurIA()
    print("Coup de l'IA :", ia.prochain_coup(grille.tab, "O"))
    humain = JoueurHumain()
    print("Coup du joueur :", humain.prochain_coup(grille.tab, "X"))
