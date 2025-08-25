from collections import defaultdict
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0

        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        # Declare our array along with base cases
        dp = [0] * (max_number + 1)
        dp[1] = points[1]

        for num in range(2, len(dp)):
            # Apply recurrence relation
            dp[num] = max(dp[num - 1], dp[num - 2] + points[num])
        
        return dp[max_number]
    

s = Solution()
print(s.deleteAndEarn([3,4,2]))
print(s.deleteAndEarn([2,2,3,3,3,4]))