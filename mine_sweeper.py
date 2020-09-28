"""
Write a function that will take 3 arguments
1)bombs =  list of bomb locations in the format [row, column]
2)rows
3)columns

mine_sweeper([[0,0], [1,2]], 3, 4)

bomb is at row index 0 column index 0
bomb is at row indes 1 column index 2

3 rows
4 columns


we should have a 3 x 4 array and -1 should represent bomb locations in the returned matrix

"""


def mine_sweeper(bombs, rows, cols):
    field = [[0 for i in range(rows)] for j in range(cols)]

    for bomb_location in bombs:
        (bomb_row, bomb_col) = bomb_location
        field[bomb_row][bomb_col] = -1

    return field


print(mine_sweeper([[1, 3], [3, 2], [2, 3]], 4, 4))
