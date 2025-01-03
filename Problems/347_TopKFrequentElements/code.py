from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counterDict = {} # hashmap where key = number, value = count
    topKList: List[int] = [] # final list to return

    # T: O(n)
    # S: O(n)
    for i in nums:
        # if exists in the dict, increment count
        # otherwise, if doesn't exist in dict, create entry with count of 1
        if i in counterDict:
            print("In the dict.")
            counterDict[i] += 1
        else:
            print("Not in the dict.")
            counterDict[i] = 1
        
    # sort the dictionary by value (the item count)
    # T: timsort is O(n log n), at best
    # S: O(1n)
    s = list(sorted(counterDict.items(), key=lambda item: item[1], reverse=True))
    print("Sorted dictionary as list:")
    print(s)

    # return the top k elements from the sorted dictionary
    # T: O(k) which is potentially O(n)
    # S: O(n)
    for j in range(k):
        print(s[j][0])
        topKList.append(s[j][0])
    
    print("TopKList:")
    print(topKList)

    return topKList

a = topKFrequent([1,1,1,2,2,3], 2)
print(a)

b = topKFrequent([1], 1)
print(b)

# T: O(n log n) but technically O(n + nlogn + k) => O(nlogn)
# S: O(3n)