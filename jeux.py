import random

def demander_nombre(nb_min,nb_max):
    nbre_int = 0
    while nbre_int == 0:
        nbre_str = input(f"Quel est le nombre magique entre {nombre_min} et {nombre_max} : ")
        try:
            nbre_int = int(nbre_str)
        except:
            print("Vous devez entrer un nombre.reessayez !")
        else:
            if nbre_int < nb_min or nbre_int > nb_max:
                print(f"Erreur: Le nombre doit etre compris entre {nb_min} et {nb_max}.Reessayez! ")
                nbre_int = 0
    return nbre_int
nombre_min = 1
nombre_max = 10
nombre_magic = random.randint(nombre_min,nombre_max)
nbre_de_vies = 4

nombre = 0
vies = nbre_de_vies
while not nombre == nombre_magic and vies>0:
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(nombre_min,nombre_max)

    if nombre == nombre_magic:
        print("Bravo, vous avez gagne")
    elif nombre > nombre_magic:
        print("plus petit !")
        vies -= 1
    else:
        print("plus grand !")
        vies -= 1
if vies == 0:
    print(f"Vous avez perdu ! le nombre correcte etait : {nombre_magic}")