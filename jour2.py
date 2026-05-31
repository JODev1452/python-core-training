
# Samedi 28 février 2026 (10:49)

# ACTIVITÉ : Algorithmique et programmation en Python

# Partie A

# Exercice 1 : Entrainement sur Git et GitHub
# - Créons un repo local pour ce projet et ajoutons-y ce fichier "jour2.py".
# - Créons un fichier texte "notes.txt" et ajoutons-y quelques notes sur ce que nous avons appris jusqu'à présent.
# - Commitons ces changements avec un message de commit approprié.

# PROJET : Gestionnaire de notes

def afficher_menu():
    print("Menu :")
    print("1. Ajouter un étudiant et sa note")
    print("2. Afficher les notes")
    print("3. Supprimer une note")
    print("4. Quitter")

def ajouter_note(notes):
    nom = input("Entrez le nom de l'étudiant : ")
    try:
        note = float(input("Entrez la note de l'étudiant : "))
        notes[nom] = note
        print("Note ajoutée avec succès !")
    except ValueError:
        print("Veuillez entrer une note valide.")

def afficher_notes(notes):
    if not notes:
        print("Aucune note à afficher.")
        return
    for nom, note in notes.items():
        print(f"{nom} : {note}")

def supprimer_note(notes):
    nom = input("Entrez le nom de l'étudiant dont vous souhaitez supprimer la note : ")
    if nom in notes:
        del notes[nom]
        print("Note supprimée avec succès !")
    else:
        print("Étudiant non trouvé.")

def main():
    notes = {}
    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")
        if choix == '1':
            ajouter_note(notes)
        elif choix == '2':
            afficher_notes(notes)
        elif choix == '3':
            supprimer_note(notes)
        elif choix == '4':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()


