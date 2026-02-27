
# Vendredi 27 février 2026

# ACTIVITÉ : Algorithmique et programmation en Python

# Partie A 

# Exercice 1 : Ecrire une fonction retournant un dictionnaire contenant les éléments d'une liste ("max", "min", "moyenne", "nombre_pairs", "nombre_impairs") et leurs valeurs respectives.
def analyse_liste(nombres):
    if not nombres:
        return {"max": None, "min": None, "moyenne": None, "nombre_pairs": 0, "nombre_impairs": 0}
    max_val = max(nombres)
    min_val = min(nombres)
    moyenne = sum(nombres) / len(nombres)

    pairs = sum(1 for n in nombres if n % 2 == 0)
    impairs = len(nombres) - pairs

    return {"max": max_val, "min": min_val, "moyenne": moyenne, "nombre_pairs": pairs, "nombre_impairs": impairs}
# Demander à l'utilisateur de saisir une liste de nombres
input_str = str(input("Entrez une liste de nombres séparés par des espaces : "))
nombres = [int(x) for x in input_str.split()]
resultat = analyse_liste(nombres)
print(resultat)

# Exercice 2 : Anagramme
def sont_anagrammes(mot1, mot2):
    return slicing(mot1) == slicing(mot2)
def slicing(mot):
    return slicing(mot[1:]) + mot[0] if mot else ""
# Demander à l'utilisateur de saisir deux mots
nom = input("Rappelez votre nom : ")
print(f"Ok, bienvenue {nom} !")
mot1 = input(f"{nom}, donne un premier mot :")
mot2 = input(f"{nom}, donne maintenant le second mot : ")
print("")
print(f"Merci, beaucoup {nom} !")
if sont_anagrammes(mot1, mot2):
    print(f"{mot1} et {mot2} sont des anagrammes.")
else:
    print(f"{mot1} et {mot2} ne sont pas des anagrammes.")
print("")
# Fin de la partie A


