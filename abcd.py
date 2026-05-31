# Programme du jour : Liste de courses

# Date : 2026-05-05

print("")
print("")
print("---")
print("")
print("BIENVENUE DANS LE PROGRAMME DU JOUR : LISTE DE COURSES")
print("")
print("---")
print("")
print("")

print("")
print("Aujourd'hui, nous allons créer une liste de courses interactive en Python.")
print("")
nom = input("Avant de commencer, quel est votre nom ? ")
print("")
print(f"Alors {nom}, commençons !")

print("")

def creer_liste_courses():
    liste = []

    for i in range(3):
        article = input(f"{nom}, Entrez un article à ajouter à votre liste de courses : ")
        liste.append(article)

    return liste

print("")

liste_courses = creer_liste_courses()
print(f"{nom}, voici votre liste de courses : {liste_courses}") 

retirer = input(f"{nom}, avez-vous un ou des articles à retirer de votre liste de courses ? (Oui/Non) : ")

if retirer.lower() == "oui":
    article_retirer = input(f"{nom}, Quel est le ou l'article à retirer ? : ")

    if article_retirer in liste_courses:
        liste_courses.remove(article_retirer)
        print(f"{nom}, vous avez retiré {article_retirer} de votre liste de courses.")
    else:
        print("Cet article n'est pas dans votre liste de courses.")

print("")


print(f"{nom}, voici votre liste de courses finale : {liste_courses}")
print("")

print("")
print("Merci d'avoir utilisé ce programme pour créer votre liste de courses !")

print("")
print(f"A bientôt, {nom} !")
print("")

print("")
print("---")
print("")