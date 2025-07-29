from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        dp = [[1] * _ for _ in range(1, numRows + 1)]

        for row in range(2, numRows):
            for cell in range(1, len(dp[row]) - 1):
                dp[row][cell] = dp[row - 1][cell - 1] + dp[row - 1][cell]


        return dp
    
s = Solution()
print(s.generate(5))
# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(s.generate(1))
# [[1]]