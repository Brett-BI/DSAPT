from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        dp = [0] * len(nums)

        # base cases?

        # always start at 0 and we have to dynamically update our index
        position = 0

        while position < len(nums):
            dp[position] = False
            if nums[position] == 0:
                return False
            nextPosition = position + nums[position]
            if nextPosition < len(nums) - 1:
                position = nextPosition
            elif nextPosition == len(nums) - 1:
                return True
            else:
                return False
            
        
        return False


s = Solution()
print(s.canJump([2,3,1,1,4])) # true
print(s.canJump([3,2,1,0,4])) # false
print(s.canJump([0]))
print(s.canJump([1]))
print(s.canJump([2,0]))