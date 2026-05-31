
# Programme : Demo Mot de passe
# PROJET : GESTIONNAIRE DE TACHES AVANCE

def afficher_menu():
    print("Menu :")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Marquer une tâche comme terminée")
    print("4. Supprimer une tâche")
    print("5. Quitter")

def ajouter_tache(taches):
    tache = input("Entrez la description de la tâche : ")
    taches.append({"description": tache, "terminee": False})
    print("Tâche ajoutée avec succès !")

def afficher_taches(taches):
    if not taches:
        print("Aucune tâche à afficher.")
        return
    for index, tache in enumerate(taches):
        statut = "Terminé" if tache["terminee"] else "En cours"
        print(f"{index + 1}. {tache['description']} - {statut}")

def marquer_tache_terminee(taches):
    afficher_taches(taches)
    if not taches:
        return
    try:
        index = int(input("Entrez le numéro de la tâche à marquer comme terminée : ")) - 1
        if 0 <= index < len(taches):
            taches[index]["terminee"] = True
            print("Tâche marquée comme terminée !")
        else:
            print("Numéro de tâche invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

def supprimer_tache(taches):
    afficher_taches(taches)
    if not taches:
        return
    try:
        index = int(input("Entrez le numéro de la tâche à supprimer : ")) - 1
        if 0 <= index < len(taches):
            del taches[index]
            print("Tâche supprimée avec succès !")
        else:
            print("Numéro de tâche invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

def main():
    taches = []
    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")
        if choix == '1':
            ajouter_tache(taches)
        elif choix == '2':
            afficher_taches(taches)
        elif choix == '3':
            marquer_tache_terminee(taches)
        elif choix == '4':
            supprimer_tache(taches)
        elif choix == '5':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
nom = "Onesime"

for i in range(3):
    mot_de_passe = input("Entrez votre mot de passe : ")
    if mot_de_passe == "python123":
        print(f"Bienvenue {nom} !")
        break
    else:
        print("Mot de passe incorrect")
else:
    print("Trop de tentatives, accès bloqué.")

