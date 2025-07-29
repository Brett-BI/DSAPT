from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}

        for a in arr:
            if a in counts.keys():
                counts[a] = counts[a] + 1
            else:
                counts[a] = 1

        tally = set()
        for c in counts:
            if counts[c] in tally:
                return False
            else:
                tally.add(counts[c])

        return True


s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))
print(s.uniqueOccurrences([1,2]))
print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))




# counters = []
# for num in set(arr):
#     counters.append(arr.count(num))
# return len(set(counters)) == len(counters) 