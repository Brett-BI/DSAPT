from typing import List


class Solution:
    def __init__(self):
        pass

    def robIterative(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)

        # base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # recurrence relation
            # this is calculating the maximum loot at the current index based on 
            # the loot previously acquired by checking two possibilities: 
            # the current house + house at index - 2 (skip one to avoid the alarm)
            # or the previous index (meaning that we're only taking that value)
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    def robMemo(self, nums: List[int]) -> int:
        def dp(i):
            # Base cases
            if i == 0: 
                memo[i] = nums[0]
                return nums[0]            
            if i == 1: 
                memo[i] = max(nums[0], nums[1])
                return max(nums[0], nums[1])            
            if i not in memo:
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i]) # Recurrence relation
            return memo[i]
        
        memo = {}
        return dp(len(nums) - 1)
    
s = Solution()
print(s.robIterative([1,9,5,5,3,9,12,3]))

'''
1,9,5,5,3,9,12,3

0,0,0,0,0,0,0,0
0,9,0,0,0,0,0,0
0,9,9,0,0,0,0,0 n: 2, max: 9 or 0 + 5?
0,9,9,0,0,0,0,0 n: 3, max: 9, 9 + 5?
0,9,9,14,0,0,0,0 n: 4, max: 14, 9 + 3?
0,9,9,14,14,0,0,0 n: 5, max: 14, 14 + 9?
0,9,9,14,14,23,0,0 n: 6, max: 23, 14 + 12?
0,9,9,14,14,23,26,0 n: 7, max: 26, 23 + 3?
0,9,9,14,14,23,26,26
ans = 26?
'''