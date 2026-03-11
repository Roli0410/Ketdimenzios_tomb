matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# print(matrix[1][1])

for sor in matrix:
    # print(sor)
    for oszlop in sor:
        print(oszlop, end=" ")
    print()

for i in range(0, len(matrix)):
    print(matrix[i])
    for j in range(0, len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

