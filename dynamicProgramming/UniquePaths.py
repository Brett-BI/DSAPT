def uniquePaths(m: int, n: int) -> int:
    # create a table filled with 0s
    board = [[0] * n for _ in range(m)]
    # print("Board initialized:")
    # print(board)

    # initialize right- and bottom-most columns
    for i in range(m):        
        board[i][n - 1] = 1
        # print("~~~~~~(i)~~~~~~")
        # print(board)
    
    for j in range(n):
        board[m - 1][j] = 1
    #     print("~~~~~~(j)~~~~~~")
    #     print(board)

    # print("\nBoard is now:")
    # print(board)

    # fill in from the bottom up
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            # if !isObstacle():
            board[i][j] = board[i + 1][j] + board[i][j + 1]
            # print("\n--------- i: {}, j: {} --------".format(i, j))
            # print(board)
    
    # return result in lower corner
    return board[0][0]

answer = uniquePaths(3, 2)
print(answer)