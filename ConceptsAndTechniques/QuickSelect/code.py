import random
from typing import List


def quickSelect(arr: List[int], low: int, high: int, k: int) -> int:
    if low <= high:
        pivot_index: int = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return quickSelect(arr, low, pivot_index - 1, k)
        else:
            return quickSelect(arr, pivot_index + 1, high, k)

def partition(arr: List[int], low: int, high: int) -> int:
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
