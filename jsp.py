# Créé par E20220032, le 18/01/2023 en Python 3.7
N=int(input())
print ("N est de", N)
while N>1:
    DIV=2
    while N % DIV != 0:
        DIV = DIV +1
    N=N/DIV
    print(DIV)

