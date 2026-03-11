tabla = [
    ['X', 'O', None],
    [None, 'X', 'O'],
    ['O', None, 'X']
]

for i in range(0, len(tabla)):
    for j in range(0, len(tabla[i])):
        if tabla[i][j] == None:
            print("_", end=" ")
        else:
            print(tabla[i][j], end=" ")
    print()

print("\n")

tabla[0][2] = "O"


for i in range(0, len(tabla)):
    for j in range(0, len(tabla[i])):
        if tabla[i][j] == None:
            print("_", end=" ")
        else:
            print(tabla[i][j], end=" ")
    print()