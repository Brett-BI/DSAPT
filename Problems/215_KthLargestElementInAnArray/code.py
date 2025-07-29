import heapq
import random
from typing import List


class Solution:
    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0] 
    
    # QuickSelect is normally used to find the kth SMALLEST element
    # Since we need the kth LARGEST, we need to swap left and right
    # T: O(N), S: O(1)
    def findKthLargestQuickSelect(self, nums: List[int], k: int) -> int:
        def quickSelect(nums: List[int], k: int) -> int: 
            pivot = random.choice(nums)
            left, mid, right = [], [], [] # fine because it's all the same type, I guess

            # num > pivot to left, num < pivot to right so that the resulting lists are 
            # arranged in a way that the left list contains the larger elements and the 
            # right list is contains the smaller elements
            for num in nums:
                if num > pivot: # normally append to right
                    left.append(num)
                elif num < pivot: # normally append to left
                    right.append(num)
                else:
                    mid.append(num) # in case our num in also our pivot and all dups

            # left contains larger elements, so recurse with larger element list
            # until we have our k largest nmnm elements
            if k <= len(left):
                return quickSelect(left, k)
            
            # we have the k largest elements in left plus mid/pivot and it's duplicates
            # length of left and length of mid is less than k, we still have to wittle 
            # the list down; we need to select the smallest element from the list which is 
            # always going to split to the right
            # decrement k so we are constantly wittling the size of the list to 1
            # when len(mid) = 1, len(left) = 1, this will fail and we can return the last item
            if len(left) + len(mid) < k:
                return quickSelect(right, k - len(left) - len(mid))
            
            return pivot
        
        return quickSelect(nums, k)