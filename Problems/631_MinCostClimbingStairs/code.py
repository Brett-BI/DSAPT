from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        
        dp = [0] * (len(cost))
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for c in range(2, len(cost)):
            dp[c] = min(dp[c-1] + cost[c], dp[c-2] + cost[c])
            
        return min(dp[-1], dp[-2])
    

s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))