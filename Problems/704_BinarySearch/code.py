from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lowPointer: int = 0
        highPointer: int = len(nums) - 1
        # (len(nums) / 2) - 1

        # If lowPointer < highPointer, there are still 2+ elements to evaluate before
        # the list of numbers is exausted
        # If lowPointer = highPointer, the last item has been found and it needs to 
        # be evaluated.
        while lowPointer <= highPointer:
            # calculate the middle index between the two pointers using floor division
            mid = (lowPointer + highPointer) // 2
            t = nums[mid]

            # compare and choose next operation
            if t == target:
                return mid
            elif t < target:
                lowPointer = mid + 1 # low index is the previous mid point
            else:
                highPointer = mid - 1 # high index is the previous mid point

        return -1
    
# T: O(1) -> O(logn)
# S: O(n)
    
s1 = Solution()
a = s1.search([-1, 0, 3, 5, 9, 12], 9) # 4
print(a)
a2 = s1.search([-1, 0, 3, 5, 9, 12], 2) # -1
print(a2)
a3 = s1.search([5], 5)
print(a3)
a4 = s1.search([2, 5], 5)
print(a4)