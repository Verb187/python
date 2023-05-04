# Créé par e20220032, le 01/03/2023 en Python 3.7
def Ndiv(N):
    c = 0
    for k in range (1, N+1):
        if N % k == 0:
            c = c + 1
    return c

def NBPRE():
    P = []
    i = 2
    while len(P) != 100:
        if Ndiv(i) == 2:
            P.append(i)
        i += 1
    return P[99]

print(NBPRE())