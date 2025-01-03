def uniquePaths(m: int, n: int) -> int:
    # create a m x n matrix filled with 0s
    board = [[0] * n for _ in range(m)]

    # initialize right- and bottom-most columns
    for i in range(m):        
        board[i][n - 1] = 1
    
    for j in range(n):
        board[m - 1][j] = 1

    # fill in from the bottom up
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            board[i][j] = board[i + 1][j] + board[i][j + 1]
    
    # return result in lower corner
    return board[0][0]

answer = uniquePaths(3, 7)
print(answer)