# unique paths

from typing import List


class Solution:
    def uniquePathsBU1(self, m: int, n: int) -> int:
        # create a m x n matrix filled with 1s
        board = [[1] * n for _ in range(m)]

        for b in board:
            print(b)

        for i in range(m - 2, -1, -1): # decrement to 0 (stop is NOT inclusive)
            for j in range(n - 2, -1, -1):
                board[i][j] = board[i + 1][j] + board[i][j + 1]
        
        # return result in lower corner
        return board[0][0]

    def uniquePathsTD1(self, m: int, n: int) -> int:
        # create a board with 1s by default - important for addition operation
        board = [[1] * n for _ in range(m)]

        # loop through each cell in the matrix and calculate the paths to that cell
        # this is going to add the cell to the left and the cell above the current cell
        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = board[i - 1][j] + board[i][j - 1]

        # return the final total (last cell in the matrix)
        return board[m - 1][n - 1]
    
    def uniquePathsBU(self, m: int, n: int) -> int:
        board: List[List[int]] = [[1] * n for _ in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                board[i][j] = board[i + 1][j] + board[i][j + 1]

        return board[0][0]

    def uniquePathsTD(self, m: int, n: int) -> int:
        board: List[List[int]] = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = board[i - 1][j] + board[i][j - 1]

        return board[m - 1][n - 1]

s = Solution()
# assert s.uniquePathsBU(3,7) == 28, "FAIL: {}".format(s.uniquePathsBU(3,7))
# assert s.uniquePathsBU(3,2) == 3, "FAIL: {}".format(s.uniquePathsBU(3,2))
# print(s.uniquePathsTD(3,7))
# print(s.uniquePathsTD(2,3))

print(s.uniquePathsBU(3,7))
print(s.uniquePathsTD(3,7))
print(s.uniquePathsBU(2,3))
print(s.uniquePathsTD(2,3))
