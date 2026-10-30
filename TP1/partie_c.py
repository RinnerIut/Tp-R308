import random


def choisir_mot(liste):
    if len(liste) == 0:
        return None

    return random.choice(liste).upper()


def masque(mot):
    resultat = []

    for lettre in mot:
        resultat.append("_")

    return resultat


# Ce bloc s'exécute seulement quand on lance ce fichier directement.
if __name__ == "__main__":
    mots = ["python", "ordinateur", "reseau", "clavier"]

    mot = choisir_mot(mots)

    print("Mot choisi :", mot)
    print("Masque :", masque(mot))
    print("Test PYTHON :", masque("PYTHON"))