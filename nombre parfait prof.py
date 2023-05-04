# Créé par E20220032, le 05/10/2022 avec EduPython
from lycee import *

def nbr_parfait(n):
    s = 0
    for i in range ( 1,n):
        if(n%i==0):
          s = s + i
    if s == n :
        print (n , "est un nombre parfait")
    else:
        print (n ," n'est pas un nombre pafait ")
    return (n)
print (nbr_parfait(28))

