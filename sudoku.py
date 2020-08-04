sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

row_nu = 0  # to insert "-"
for row in sudoku:
    col_nu = 0  # to insert "|"
    row_nu+=1
    if row_nu in range(1,20,3):  # if row == 1 or row == 4 or row == 7
        print("-"*21)
    for num in rows:
        col_nu+=1
        if col_nu in range (4,20,3):  # if col == 4 or col == 7
            print("|", end=" ")
        print(num, end=" ")
    print(" ")
print("-"*21)
