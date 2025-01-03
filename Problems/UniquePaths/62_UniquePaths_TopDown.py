'''
    Top-down approach using dynamic programming.

    Cell values represent valid paths to cell.

    NOTE: no obstacles.
'''

def uniquePaths(m: int, n: int) -> int:
    # create a table filled with 1s
    board = [[1] * n for _ in range(m)] 

    # calculate paths by adding square above and square to left
    # Outside cells only ever require 1 path so start at 1
    for i in range(1, m):
        for j in range(1, n):
            # board[i][j] = current cell being evaluated
            # board[i - 1][j] = cell above of current
            # board[i][j - 1] = cell left of current
            cellAbove = board[i - 1][j]
            cellBelow = board[i][j - 1]
            board[i][j] = board[i - 1][j] + board[i][j - 1]

    # final answer always going to be in last cell of grid
    return board[m - 1][n - 1]

answer = uniquePaths(3, 7)
print(answer)

# T: O(m*n + m*n) because m and n can be different values
# technically, it's O(2(m*n)) but the constant is ignored
# S: O(m*n) because the board creation is the only thing that
# requires space.