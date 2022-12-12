#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def comparer2fichiers(fichier_1,fichier_2):
    with open(fichier_1,"r") as fichier1:
        with open(fichier_2,"r") as fichier2:

            for count, ligne in enumerate(fichier1):
                ligne_2=fichier2.readline()
                if ligne_2==ligne:
                    continue
                elif ligne_2!=ligne:
                    print("Les fichiers ne sont pas equivalents")
                    fichier2.close()
                    fichier1.close()
                    return False
    fichier2.close()
    fichier1.close()
    return True
def triplagedespace(fichier1):
    with open(fichier1,"+") as f1:
        for count,ligne in enumerate(f1):
            ligne.replace(" ","   ")
    f1.close()


    return
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    Directoire="C:\\Users\\Mael\\Documents\\GitHub\\chapitre-08-MaelPixel\\"
    print(comparer2fichiers(Directoire+"settings\\"+"essaie1.txt",Directoire+"settings\\"+"essaie2.txt"))
    pass
