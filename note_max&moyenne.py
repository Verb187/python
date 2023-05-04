# Créé par E20220032, le 18/01/2023 en Python 3.7
note_max=0
moyenne=0
tableau=[[12,15,13,7],[9,11,14,8]]

for i in range (2):
    for j in range (4):
        note= tableau [i][j]
        if ( note> note_max):
            note_max=note
        moyenne=moyenne+tableau[i][j]
print (note_max)
print(moyenne/8)
