# Créé par e20220032, le 01/02/2023 en Python 3.7
N = int (input())
liste = [(-2)** (n+1) for n in range (N)]
 print liste
MIN = 1000
s = 0
for k in range (N):
    if liste [k] < MIN:
        MIN =liste [k]
        s=s + liste[k]
 print MIN
 print S/N
