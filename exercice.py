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
    with open(fichier1,"r") as f1:
        data=f1.readlines()
        for count,ligne in enumerate(data):
            data[count]=ligne.replace(" ","   ")
    f1.close()
    with open(fichier1,"w") as f1:
        f1.writelines(data)
    return f1
def assignationdenote(fichier,tableau):
    with open(fichier,"r") as f:
        data=f.readlines()
        for note in data:
            for key in tableau:
                notetrier=note.replace("\n","")
                bareme=tableau[key][0]
                if int(notetrier)-bareme<0:
                    continue
                elif int(notetrier)-bareme>0:
                    data[data.index(note)]=f"{key},{note}"
                    break
    f.close()
    with open(fichier,"w") as f:
        f.writelines(data)
    return f
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    Directoire="C:\\Users\\Mael\\Documents\\GitHub\\chapitre-08-MaelPixel\\"
    #print(comparer2fichiers(Directoire+"settings\\"+"essaie1.txt",Directoire+"settings\\"+"essaie2.txt"))
    #print(triplagedespace(Directoire+"settings\\essaie1.txt"))
    print(assignationdenote(Directoire+"notes.txt",PERCENTAGE_TO_LETTER))
    pass
