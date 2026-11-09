# TP3 - Gestion d'une bibliothèque

Depuis la racine du dépôt, avec Python 3.10 ou plus :

- `python TP3/partie_a.py` : exemple avec un livre et un utilisateur.
- `python TP3/partie_b.py` : exemple de gestion de la bibliothèque.
- `python TP3/partie_c.py` : exemple de sauvegarde et de rechargement CSV.
- `python TP3/partie_d.py` : menu complet de la bibliothèque.

Les parties réutilisent les fichiers précédents : conserver tous les fichiers ensemble.
La partie C ajoute la sauvegarde à la classe Bibliotheque de la partie B par héritage.

Le menu charge automatiquement les données au lancement. Choisir **6** pour
sauvegarder et quitter. Sans sauvegarde existante, la bibliothèque démarre vide.

Les données du menu sont dans `TP3/bibliotheque.csv` (livres et emprunts) et
`TP3/bibliotheque_utilisateurs.csv` (utilisateurs, y compris sans emprunt).
Le CSV des livres contient : titre, auteur, annee, disponible, emprunteur.
La démonstration de la partie C utilise des fichiers séparés, préfixés par `exemple_`.
Ces fichiers de données sont créés à l'exécution et ne sont pas envoyés sur GitHub.
