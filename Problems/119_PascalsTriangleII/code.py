from typing import List


class Solution:
    def generate(self, numRows: int) -> List[int]:

        dp = [[1] * _ for _ in range(1, numRows + 2)]
        print(dp)

        for row in range(2, numRows + 1):
            for cell in range(1, len(dp[row]) - 1):
                val = dp[row - 1][cell - 1] + dp[row - 1][cell]
                print(f"Value is: ${dp[row - 1][cell - 1]} + ${dp[row - 1][cell]} = ${val}")
                dp[row][cell] = val


        return dp[-1]
    
s = Solution()
print(s.generate(3))
# [1,3,3,1]
print(s.generate(0))
# [1]
print(s.generate(1))
# [1,1]