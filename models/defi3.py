"""
Compteur de scrabble
"""
# Voici la clé de correspondance (un dictionnaire)
# lettre:valeur pour calculer le score d'un mot
score = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
         "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
         "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
         "y": 4, "z": 10}


# Créer une fonction pour
# calculer le score du mot
def calculer_score(mot):
    """Calculer le score du mot
    en fonction de la valeur de ses lettres."""
    # Mettre le mot en minuscule
    # pour chercher dans le dictionnaire plus haut
    try:
        mot2 = mot.lower()
    except Exception:
        mot2 = ""
    # Créer un objet de départ
    points = 0
    # Pour chaque lettre l dans
    # la chaine de caractères mot2
    for lettre in mot2:
        # Si la lettre l égale
        # la lettre l convertie en chaine d'un caractère avec
        # str() pour string
        # Ce contrôle de qualité
        # élimine les chiffres, car ils sont
        # convertir en texte (1 devient "1" ou '1')
        if lettre == str(lettre):
            # Extraire la valeur de la lettre
            # du dictionnaire score
            # Ajouter cette valeur à la variable points
            # Chaque itération ajoute une nouvelle valeur
            # À la fin de la boucle, l'objet points
            # a accumulé toutes les valeurs de chaque
            # lettre du mot évalué
            try:
                points += score[lettre]
            except Exception:
                points += 0
    # Retourner le total calculé
    return mot2 + ": " + str(points)


if __name__ == "__main__":
    # Imprimer un espace et un diviseur
    print("")
    print("------------------------")

    # Invoquer la fonction calculer_score
    # pour évaluer le score de mots...
    # Imprimer le résultat
    print(calculer_score("allo"))
    print(calculer_score("xylophone"))
    print(calculer_score("yak"))
    print(calculer_score(""))
    print(calculer_score("123"))
    print(calculer_score(True))
