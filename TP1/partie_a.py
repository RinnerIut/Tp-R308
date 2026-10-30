# Ajouter un étudiant ou modifier sa note
def ajouter_etudiant(d, nom, note):
    try:
        d[nom] = float(note)
    except (ValueError, TypeError):
        print("La note doit être un nombre.")


def moyenne_classe(d):
    if len(d) == 0:
        return 0

    total = 0
    for note in d.values():
        total = total + note

    return total / len(d)


def meilleur_etudiant(d):
    meilleur = None

    for nom in d:
        if meilleur is None or d[nom] > d[meilleur]:
            meilleur = nom

    if meilleur is None:
        return None

    return (meilleur, d[meilleur])


# Écrire une ligne nom:note pour chaque étudiant
def sauvegarder(d, fichier):
    try:
        with open(fichier, "w", encoding="utf-8") as f:
            for nom in d:
                f.write(nom + ":" + str(d[nom]) + "\n")
    except OSError:
        print("Impossible de sauvegarder le fichier.")


def recharger(fichier):
    d = {}

    try:
        with open(fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                try:
                    # Séparer le nom et la note au niveau du :
                    nom, note = ligne.strip().split(":")
                    if nom != "":
                        d[nom] = float(note)
                except ValueError:
                    print("Ligne incorrecte ignorée.")
    except (OSError, UnicodeError):
        print("Fichier absent ou impossible à lire.")

    return d


# Programme principal
etudiants = {}

ajouter_etudiant(etudiants, "Alice", 12)
ajouter_etudiant(etudiants, "Bob", 15)
ajouter_etudiant(etudiants, "Claire", 9.5)

print("Étudiants :", etudiants)
print("Moyenne :", round(moyenne_classe(etudiants), 2))
print("Meilleur étudiant :", meilleur_etudiant(etudiants))

sauvegarder(etudiants, "etudiants.txt")
print("Étudiants rechargés :", recharger("etudiants.txt"))

    