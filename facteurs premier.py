# Créé par E20220032, le 18/01/2023 en Python 3.7
def factor (N):
    L = []
    DIV = 2
    while N > 1:
        if N % DIV==0 :
            L.append(DIV)
            N= N // DIV
        else :
            DIV =  DIV + 1
    return L
print(factor (14))

# factor sert a trouver les facteurs premiers d'un nombre
# factor(14) = [2,7]


