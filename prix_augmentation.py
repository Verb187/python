# Créé par E20220032, le 21/09/2022 en Python 3.7
from lycee import*
def pantalon():
    p = 100
    L = []
    for K in range (1.10):
        p = 1.04 * p
        L.append (p)
    return (L)
print (pantalon(5))
