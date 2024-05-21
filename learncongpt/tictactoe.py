

def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 9)

def coup_valide(plateau, ligne, colonne):
    return plateau[ligne][colonne] == ' '

def coup_gagnant(plateau, symbole):
    # Vérification des lignes et colonnes
    for i in range(3):
        if all(plateau[i][j] == symbole for j in range(3)) or all(plateau[j][i] == symbole for j in range(3)):
            return True

    # Vérification des diagonales
    if all(plateau[i][i] == symbole for i in range(3)) or all(plateau[i][2 - i] == symbole for i in range(3)):
        return True

    return False

def plateau_complet(plateau):
    return all(plateau[i][j] != ' ' for i in range(3) for j in range(3))

def minimax(plateau, profondeur, joueur_max):
    symbole_ordi = 'O' if joueur_max else 'X'

    if coup_gagnant(plateau, 'O'):
        return 1
    elif coup_gagnant(plateau, 'X'):
        return -1
    elif plateau_complet(plateau):
        return 0

    if joueur_max:
        meilleur_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if plateau[i][j] == ' ':
                    plateau[i][j] = symbole_ordi
                    score = minimax(plateau, profondeur + 1, False)
                    plateau[i][j] = ' '
                    meilleur_score = max(meilleur_score, score)
        return meilleur_score
    else:
        pire_score = float('inf')
        for i in range(3):
            for j in range(3):
                if plateau[i][j] == ' ':
                    plateau[i][j] = 'X'
                    score = minimax(plateau, profondeur + 1, True)
                    plateau[i][j] = ' '
                    pire_score = min(pire_score, score)
        return pire_score

def meilleur_coup(plateau):
    meilleur_score = float('-inf')
    meilleur_coup = None

    for i in range(3):
        for j in range(3):
            if plateau[i][j] == ' ':
                plateau[i][j] = 'O'
                score = minimax(plateau, 0, False)
                plateau[i][j] = ' '

                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = (i, j)

    return meilleur_coup

def jeu_morpion():
    plateau = [[' ' for _ in range(3)] for _ in range(3)]
    tour_ordi = False

    while True:
        afficher_plateau(plateau)

        if tour_ordi:
            ligne, colonne = meilleur_coup(plateau)
            print("L'ordinateur joue en ({}, {})".format(ligne, colonne))
        else:
            while True:
                try:
                    ligne = int(input("Entrez le numéro de ligne (0, 1, 2) : "))
                    colonne = int(input("Entrez le numéro de colonne (0, 1, 2) : "))
                    if 0 <= ligne < 3 and 0 <= colonne < 3 and plateau[ligne][colonne] == ' ':
                        break
                    else:
                        print("Coup invalide. Veuillez réessayer.")
                except ValueError:
                    print("Veuillez entrer un nombre entier.")

        symbole = 'O' if tour_ordi else 'X'
        plateau[ligne][colonne] = symbole

        if coup_gagnant(plateau, symbole):
            afficher_plateau(plateau)
            if tour_ordi:
                print("L'ordinateur gagne !")
            else:
                print("Vous gagnez !")
            break
        elif plateau_complet(plateau):
            afficher_plateau(plateau)
            print("Match nul !")
            break

        tour_ordi = not tour_ordi

if __name__ == "__main__":
    jeu_morpion()
