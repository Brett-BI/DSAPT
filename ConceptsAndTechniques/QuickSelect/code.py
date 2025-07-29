import random
from typing import List

def qs(arr: List[int], k: int):
    # call partition
    def LomutoPartition(arr, leftLimit, rightLimit):
        return

    if k > len(arr) or k < 0:
        return None

    left = 0
    right = len(arr) - 1

    if left == right:
        return left
    
    return LomutoPartition(arr, left, right)

    return # ... eventually

def LomutoPartition(arr: List[int], leftLimit: int, rightLimit: int, k: int) -> int:
    """
    Uses the Lomuto partitioning algorithm to partition a list of integers for 
    use in the quick select algorithm. Organizes the items around a pivot, then 
    recurses until the pivot is at k.

    Parameters:
    arr (List[int]): the list of integers being partitioned
    leftLimit (int): 

    Returns:
    i (int): position of the pivot/mid-point for this particular attempt at partitioning
    """
    # choose a random pivot; it doesn't matter
    pivot: int = arr[rightLimit]
    # set starting positions for something that's 2-pointerish
    # finder moves through the array
    # replacer tracks the location for swaps
    finder = replacer = leftLimit

    # two pointerish iteration
    while finder < rightLimit:
        # if the value at the finder (the moving) index is less than the pivot, 
        # swap the positions so that values > the value at pivot index are to 
        # the right of the pivot index and values < the value at the pivot index 
        # are to the left of the pivot index
        if arr[finder] < arr[pivot]:
            arr[finder], arr[replacer] = arr[replacer], arr[finder]
            replacer += 1
        
        finder += 1
    
    # change the values at the finder and replacer indexes 
    arr[finder], arr[replacer] = arr[replacer], arr[finder]
    pivot = replacer

    return pivot

    """
    # if the pivot is at k, the position that we want to find (i.e. "kth")
    if pivot == k:
        return pivot
    # if the pivot is > k, or to the right of the position we're trying to find
    elif pivot > k:
        # partition again using the previous leftLimit as the start and the value 
        # of pivot - 1 as the rightLimit
        return LomutoPartition(arr, leftLimit, pivot - 1)
    else:
        return LomutoPartition(arr, pivot + 1, rightLimit)
    """




# Hoare's
def quickSelect(arr: List[int], low: int, high: int, k: int) -> int:
    if low <= high:
        pivot_index: int = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return quickSelect(arr, low, pivot_index - 1, k)
        else:
            return quickSelect(arr, pivot_index + 1, high, k)

def partitionHoare(arr: List[int], low: int, high: int) -> int:


def partitionLomuto(arr: List[int], low: int, high: int) -> int:
    pivot: int = arr[high]
    i: int = low

    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]

    return i

def findElement(arr: List[int], k: int) -> int:
    # Use k - 1 because the prompt probably isn't for 0-based indexing
    return quickSelect(arr, 0, len(arr) - 1, k - 1)



"""
With duplicates:
"""

def quickSelectWithDups(arr: List[int], k: int) -> int:
    # this splits the array and returns rather than using a partition() function
    pivot = random.choice(arr)
    left, mid, right = [], [], []

    for num in arr:
        if num > pivot:
            left.append(num)
        elif num < pivot:
            right.append(num)
        else:
            mid.append(num)

    if k <= len(left):
        return quickSelectWithDups(left, k)
    
    if len(left) + len(mid) < k:
        return quickSelectWithDups(right, k - len(left) - len(mid))
    

    return pivot



class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            if k <= len(left):
                return quick_select(left, k)
            
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            
            return pivot
        
        return quick_select(nums, k)
    
    def partition(arr, l, r):
        pivot = random.choice(arr)
        left, mid, right = [], [], []

        for a in arr:
            if a > pivot:
                left.append(a)
            elif a < pivot:
                right.append(a)
            else:
                mid.append(a)
        
        return pivot



def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1

    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i + 1], arr[r] = arr[r], arr[i + 1]

def kthSmallest(arr, l, r, k) -> int:
    if l == r:
        return arr[l]

    pivot = partition(arr, l, r)
    i = pivot - l + 1

    if i == k:
        return arr[pivot]
    elif i > k:
        return kthSmallest(arr, l, pivot - 1, k)
    else:
        return kthSmallest(arr, pivot + 1, r, k - i)
    
def getKth(arr, n, k):
    return kthSmallest(arr, 0, n - 1, k)
    