# Créé par e20220032, le 01/02/2023 en Python 3.7
a= int (input("Entrer la valeur de a :"))
b= int (input ("Entrer la valeur de b :"))
q=0
while a>=b :
    a = a-b
    q= q+1
print ( "Le quotient est de " , q)
print ("Le reste est de " , a)
