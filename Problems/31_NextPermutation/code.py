from typing import List


class Solution:
    def next_permutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]: # find first where previous <= current
            i -= 1
        if i >= 0: # if i isn't out of range
            j = len(nums) - 1 # last index
            while nums[j] <= nums[i]: # find the first number at j that's greater than nums[i]
                j -= 1

            nums[i], nums[j] = nums[j], nums[i] # swap i and j values so they're ordered
        
        # at this point, the list after i is ordered high -> low BUT this isn't the correct
        # LEXICAL ordering for the next permutation. The next permutation's lexical ordering 
        # is going to be based on the lexical ordering of elements after i.
        # [1,4,3,2] > [2,4,3,1] > [2,1,3,4] because 4 doesn't lexically come after 2.
            self.reverse(nums, i + 1)

    def reverse(self, nums: List[int], startIndex: int) -> None:
        endIndex: int = len(nums) - 1
        while startIndex < endIndex: # if start == end, there's nothing to swap
            nums[startIndex], nums[endIndex] = nums[endIndex], nums[startIndex]
            startIndex += 1
            endIndex -= 1

s = Solution()
p = [3,2,1]
s.next_permutation(p)
print(p)