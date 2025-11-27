"""
Exercice permettant de savoir si une phrase est un palindrome ou non

Modules:
ispalindrome(p)
main()

"""
import string

#### Fonction secondaire

TR1 = str.maketrans("ÀÁÂÄÅÇÈÉÊËÌÍÎÏÔÖÙÛÜŸàáâäçèéêëîïôöûüñ", "aaaaaceeeeiiiioouuuyaaaaceeeeiioouun")
TR2 = str.maketrans(string.punctuation, "                                ")
#print(string.punctuation)

def ispalindrome(p):

    # votre code ici
    """

    Fonction verifiant si le mot p est un palindrome
    Args:
    p: une chaine de caractères

    Returns:
    un booléen, true si la chaine de caractères est un palindrome, false sinon

    """
    print(p)
    p = p.lower().translate(TR1).translate(TR2).replace(" ","")
    print(p)
    if len(p)==1:
        return True
    if p=="":
        return True
    if p[0]==p[-1]:
        return ispalindrome(p[1:-1])
    return False

    #### Fonction principale
def main():
    """
    Tests de mots

    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
