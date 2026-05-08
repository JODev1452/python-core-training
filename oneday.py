# Programme du jour : Liste de courses

# Date : 2026-05-05

def liste():
    courses = []
    for i in range(5):
        item = input("Entrez un article à ajouter à la liste de courses : ")
        courses.append(item)
    print("Voici votre liste de courses :")

    retire = input("Avez-vous besoin de retirer un article de la liste ? ")
    if retire.lower() == "oui":
        item_retire = input("Quel article souhaitez-vous retirer ? ")
        if item_retire in courses:
            print(f"Retrait de {item_retire} de la liste.")
        else:
            print(f"{item_retire} n'est pas dans la liste.")

return liste 

liste_de_courses = liste()

print(f"Votre liste de courses finale : {liste_de_courses}")

