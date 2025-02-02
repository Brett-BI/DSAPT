from typing import List


def QuickSort2(items):
    n = len(items)
    qsort(items, 0, n - 1)

def qsort(items, low, high):
    # will always be true until there's one item left in the list
    if low < high:
        p = partition2(items, low, high)
        qsort(items, low, p - 1) # sort low, excluding the pivot
        qsort(items, p + 1, high) # sort high, excluding the pivot

# breaks the collection into low and high collections, based on pivot
# returns the index of the last item < pivot
def partition2(items, low, high):
    pivot = items[high] # or items[random.choice(len(items))]
    i = low

    # loop through elements in the range
    # two-pointer technique to place an item < pivot at/near the beginning
    # of the collection (swapping, essentially)
    for j in range(low, high):
        if items[j] < pivot:
            items[i], items[j] = items[j], items[i] # swap places
            i += 1
    
    # remember pivot is the last element in the list
    # this places it at index i so it is in its proper place in the collection
    items[i], items[high] = items[high], items[i]

    return i

ac = [3,4,6,1,9,5,7]
print(QuickSort2(ac))
print(ac)


# Modifies the list in place. It is not a stable sort because items are moved 
# to the beginning of the list repeatedly.
def sort(items: List[int]) -> None:
    size: int = len(items)
    quickSort(items, 0, size - 1)

# Recursive function call; gets the pivot of the partitioned collection
# Then recurses over the left and right partitions;
# NOTE: each call to partition() puts the pivot value in its rightful place 
# in the collection. This is why recursive calls do not include the pivot.
def quickSort(items: List[int], lowerBound: int, upperBound: int) -> None:
    if lowerBound < upperBound:
        pivot: int = partition(items, lowerBound, upperBound)
        quickSort(items, lowerBound, pivot - 1) # sort left partition, no pivot
        quickSort(items, pivot + 1, upperBound) # sort right partition, no pivot

# Use two-pointer to place all items < pivot at the beginning of the collection
# Return the index of the pivot
def partition(items: List[int], lowerBound: int, upperBound: int) -> int:
    pivot: int = items[upperBound]
    i: int = lowerBound # pointer

    for j in range(lowerBound, upperBound): # pointer
        if items[j] < pivot:
            # swap using tuple unpacking; no need for holding variable
            items[j], items[i] = items[i], items[j]
            i += 1

    # Pivot is the last item in the collection; put it in its rightful place,
    # which is at i, the last item that is < pivot.
    items[i], items[upperBound] = items[upperBound], items[i]

    return i
    
sortMe = [3,4,6,1,9,5,7]
print(sort(sortMe))
print(sortMe)