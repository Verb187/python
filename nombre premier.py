# Créé par e20220032, le 01/03/2023 en Python 3.7
# nombre premier

def est_premier(n):
     for i in range (2,n):
         if (n%i==0):
             return False
     return True
print (est_premier(7))