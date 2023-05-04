N = int(input("Entrez un nombre entier : "))

S = 0
for k in range(1, N+1):
    S += 1/k

print("Pour N =", N, ", la valeur de S est :", S)