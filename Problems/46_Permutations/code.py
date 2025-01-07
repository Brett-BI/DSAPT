from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr: List[int]):
            # base case
            # if curr is the same length as nums, there are no more open positions to fill
            if len(curr) == len(nums):
                ans.append(curr[:]) # append the entire permutation
                return

            # reducing the problem
            # for each number in nums, check if it's in curr
            for num in nums:
                if num not in curr:
                    # add the number if it's not present in curr yet
                    # meaning that it hasn't been used
                    curr.append(num)
                    backtrack(curr)
                    curr.pop() # remove and try next num at this index
            
        ans: List[int] = [] # our answer List
        backtrack([]) # start with nothing; this assumes that backtrack has access to nums

        return ans
    
    # T: O(N!)
    
s = Solution()
print(s.permute([1,2,3]))
print(s.permute([0,1]))
print(s.permute([1]))