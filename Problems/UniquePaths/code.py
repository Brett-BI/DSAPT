from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = [[1] * n for m in range(m)]
        
        print(memo)
        
        def dp(rowIndex, columnIndex):
            # if we're not at the last cell
            if (rowIndex == m - 1) or (columnIndex == n - 1):
                return memo[rowIndex - 1][columnIndex] + memo[rowIndex][columnIndex - 1]
            
            # and if the current cell has something to calculate
            if (columnIndex - 1) > -1:
                _leftValue = memo[rowIndex][columnIndex - 1]
            else:
                _leftValue = 0

            if (rowIndex - 1) > -1:
                _upperValue = memo[rowIndex - 1][columnIndex]
            else:
                _upperValue = 0

            # set the cell value
            _cellValue = _leftValue + _upperValue
            memo[rowIndex][columnIndex] = _cellValue

            # call the next recursion
            if columnIndex == n - 1:
                return dp(rowIndex + 1, 0)
            else:
                return dp(rowIndex, columnIndex + 1)
            

            return dp(0, 0)

        return dp(0,0)
    

s = Solution()
print(s.uniquePaths(3,7))
print(s.uniquePaths(3,2))


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo[r][c] will hold the number of paths from (r,c) to bottom-right
        memo = [[-1] * n for _ in range(m)]

        @cache
        def dfs(r: int, c: int) -> int:
            # 1. base case ─ reached destination
            if r == m - 1 and c == n - 1:
                return 1

            # 2. if already solved, return cached value
            if memo[r][c] != -1:
                return memo[r][c]

            # 3. explore neighbors (down, right)
            paths = 0
            if r + 1 < m:          # move down
                paths += dfs(r + 1, c)
            if c + 1 < n:          # move right
                paths += dfs(r, c + 1)

            memo[r][c] = paths     # 4. cache result
            return paths

        return dfs(0, 0)