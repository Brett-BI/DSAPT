from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)

        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]
    

s = Solution()
print(s.deleteAndEarn([3,4,2]))