#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(10000)  # Augmente la limite à 10 000


#### Fonctions secondaires

def artcode_r(string):
    """
    Retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif.

    Args:
        string (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurrences)
    """
    if not string:  # Si la chaîne est vide, on retourne une liste vide
        return []
    
    char_list = [string[0]]  # Liste des caractères rencontrés
    occurrence_list = [1]    # Liste des occurrences correspondantes
    
    for k in range(1, len(string)):
        if string[k] == string[k - 1]:
            occurrence_list[-1] += 1  # Incrémente le dernier élément des occurrences
        else:
            char_list.append(string[k])  # Ajoute un nouveau caractère
            occurrence_list.append(1)    # Ajoute une nouvelle occurrence
    return list(zip(char_list, occurrence_list))  # Combine les listes pour créer les tuples


def artcode_i(string):
    """
    Retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif.

    Args:
        string (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurrences)
    """
    if not string:  # Cas de base : chaîne vide
        return []
    
    # Trouver le nombre d'occurrences consécutives du premier caractère
    count = 1
    while count < len(string) and string[count] == string[0]:
        count += 1
    
    # Appel récursif sur la chaîne restante
    return [(string[0], count)] + artcode_i(string[count:])


#### Fonction principale

def main():
    """
    Fonction principale pour tester les fonctions itérative et récursive
    d'encodage d'une chaîne de caractères en liste de tuples.
    """
    test_string = 'MMMMaaacXolloMM'
    print(artcode_i(test_string))
    print(artcode_r(test_string))


if __name__ == "__main__":
    main()
