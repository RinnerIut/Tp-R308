# Réutiliser les fonctions de la partie C
from partie_c import choisir_mot, masque

mots = ["python", "ordinateur", "reseau", "clavier"]

mot = choisir_mot(mots)
mot_masque = masque(mot)
lettres_proposees = []
erreurs = 0

print("Jeu du pendu : 7 erreurs maximum.")

while erreurs < 7 and "_" in mot_masque:
    # Afficher le masque avec des espaces entre les lettres
    print("\nMot :", " ".join(mot_masque))
    print("Erreurs :", erreurs, "/ 7")
    print("Lettres proposées :", " ".join(lettres_proposees))

    lettre = input("Propose une lettre : ").strip().upper()

    if len(lettre) != 1 or not lettre.isalpha():
        print("Entre une seule lettre.")
        continue

    if lettre in lettres_proposees:
        print("Lettre déjà proposée.")
        continue

    lettres_proposees.append(lettre)

    if lettre in mot:
        # Révéler toutes les positions de la lettre
        for i in range(len(mot)):
            if mot[i] == lettre:
                mot_masque[i] = lettre
    else:
        erreurs = erreurs + 1
        print("Lettre absente.")

if "_" not in mot_masque:
    print("Gagné ! Le mot était", mot)
else:
    print("Perdu ! Le mot était", mot)