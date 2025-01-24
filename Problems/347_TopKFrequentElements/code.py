import heapq
from typing import List
from collections import Counter

def topKFrequentHeap(nums: List[int], k: int) -> List[int]:
    # https://realpython.com/python-counter/
    # counters are subclasses of dictionaries for counting
    c = Counter(nums)

    if k == len(nums):
        return nums
    else:
        # this is a min heap, by default, in Python
        # c.get returns the value
        # c.keys() are the keys, obviously
        # NOTE: It might behoove you to write your own sort and 
        # return the top K elements from your sorted dictionary
        # nlargest will execute c.get - iterates over c.keys() as its 
        # iterable and sort by c.get()
        return heapq.nlargest(k, c.keys(), key=c.get)
    
    return []

def topKFrequentDictionary(nums: List[int], k: int) -> List[int]:
    counterDict = {} # hashmap where key = number, value = count
    topKList: List[int] = [] # final list to return

    # T: O(n)
    # S: O(n)
    for i in nums:
        # if exists in the dict, increment count
        # otherwise, if doesn't exist in dict, create entry with count of 1
        if i in counterDict:
            counterDict[i] += 1
        else:
            counterDict[i] = 1
        
    # sort the dictionary by value (the item count)
    # T: timsort is O(n log n), at best
    # S: O(1n)
    # .items() returns a view in Python3... whatever that is. Kind of like a tuple.
    # lambda: "item:" is the name of the variable for each item the lambda operates on
    # and the "item[1]" is the return of the its second attribute (because its a tuple)
    s = list(sorted(counterDict.items(), key=lambda item: item[1], reverse=True))

    # return the top k elements from the sorted dictionary
    # T: O(k) which is potentially O(n)
    # S: O(n)
    for j in range(k):
        print(s[j][0])
        topKList.append(s[j][0])

    return topKList

a = topKFrequent([1,1,1,2,2,3], 2)
print(a)

b = topKFrequent([1], 1)
print(b)

# T: O(n log n) but technically O(n + nlogn + k) => O(nlogn)
# S: O(3n)