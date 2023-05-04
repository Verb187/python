# Créé par e20220032, le 28/09/2022 avec EduPython
from lycee import *

MYST = randint(1,100)
print ( "Le nombre mystère est de", MYST )
ESS = 0
PROP = 0
while PROP !=MYST and ESS < 5:
    print ( "Choisir un nombre ")
    PROP = int ( input  ())
    print ( "Le nombre proposé est de ", PROP )
    ESS = ESS +1
    if PROP < MYST :
        print ("Trop petit ")
    else :
        if PROP > MYST :
                print ( "Trop Grand ")
        else :
            print ("Bravo ! Vous avez gagné ")
    if ESS >= 5:
        print ( "Vous avez perdu")
print (ESS , ("essaies"))