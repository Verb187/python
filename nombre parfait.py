# Créé par e20220032, le 28/09/2022 avec EduPython
from lycee import *
#  find Perfect Number using For loop
Number = int(input(" Entrée un Nombre : "))
Sum = 0
for i in range(1, Number):
 if(Number % i == 0):
   Sum = Sum + i
if (Sum == Number):
  print(" %d est un nombre parfait " %Number)
else:
   print(" %d n'est pas un nombre parfait " %Number)
