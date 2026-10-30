import random

# Tirer un nombre entier entre 1 et 100
secret = random.randint(1, 100)
essais = 0
gagne = False

print("Devine le nombre entre 1 et 100. Tu as 10 essais.")

while essais < 10 and not gagne:
    try:
        proposition = int(input("Ton nombre : "))
    except ValueError:
        print("Entre un nombre entier.")
        continue  # Recommencer la boucle sans compter un essai

    if proposition < 1 or proposition > 100:
        print("Le nombre doit être entre 1 et 100.")
        continue

    essais = essais + 1

    if proposition < secret:
        print("Trop petit")
    elif proposition > secret:
        print("Trop grand")
    else:
        print("Gagné en", essais, "essai(s) !")
        gagne = True

if not gagne:
    print("Perdu ! Le nombre était", secret)

    