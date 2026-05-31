

# Date : 2026-31-05

print("")
print("")
print("---")
print("")
print("BIENVENUE DANS LE PROGRAMME DU JOUR : GESTIONNAIRE DE SCORE DE JEU VIDEO")
print("")
print("---")
print("")
print("")

print("")
print("En ce jour, nous allons créer un gestionnaire de score pour un jeu vidéo en Python.")
print("")

print("Xtreme, the Game")
print("      START      ")

print("")
print("Bienvenue dans Xtreme, le jeu vidéo où vous devez accumuler des points pour gagner !")
print("")

print("____INSCRIPTION DES JOUEURS____")
scores_joueurs = {}

print("")

nombre_joueurs = int(input("Entrez le nombre de joueurs participants : "))

for i in range(nombre_joueurs):
    nom_joueur = input(f"Entrez le nom du joueur {i+1} : ")
    scores_joueurs[nom_joueur] = 0

print("")


print("")

print("_____DEBUT DU JEU_____")

print("")

for partie in range(1,4):
    print(f" Score de la partie {partie} : ")

    for joueur in scores_joueurs:
        score_partie = int(
            input(f"Voici le score de {joueur} pour la partie {partie} : ")
            )
        scores_joueurs[joueur] += (
            score_partie
            )
        
    print("")

    print(f"Classement pour la partie {partie} : ")
    classement = sorted(
        scores_joueurs.items(), key=lambda x: x[1], reverse=True
    )

    for rang, (joueur, score) in enumerate(classement, 1):
        print(f"{rang} : {joueur.upper()} avec {score} points")

print("")

print("_____FIN DE LA PARTIE_____")

def vainqueur(scores):
    classement_final = sorted(
        scores.items(), key=lambda x: x[1], reverse=True
    )
    return classement_final[0][0], classement_final[0][1]

vainqueur_nom, vainqueur_score = vainqueur(scores_joueurs)

print("")

print(f"Le grand vainqueur est {vainqueur_nom.upper()} avec un score de {vainqueur_score} points !")

print("")