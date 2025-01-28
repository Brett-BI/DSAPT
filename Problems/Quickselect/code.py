# Iterative approach
def partition(arr, low, high):
    pivot = arr[high]
    i = (low - 1)
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def partition(arr, low, high):
    pivot = arr[high]
    i = (low - 1)
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def kthSmallest(a, left, right, k):
    while left <= right:
        pivotIndex = partition(a, left, right)

        if pivotIndex == k - 1:
            return a[pivotIndex]
        elif pivotIndex > k - 1:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1
        
    return -1

arr = [10,4,5,26,8,11,6]
n = len(arr)
k = 5
print(kthSmallest(arr, 0, n - 1, k))