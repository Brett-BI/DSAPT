from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(currentSubset, nextNum, size):
            if len(answer) > 0:
                if len(currentSubset) == size and currentSubset != answer[-1]:
                    answer.append(currentSubset[:])
                    return            
            else:
                answer.append([])
                return
            

            for n in range(nextNum, len(nums)):
                newSubset = currentSubset[:]
                newSubset.append(sNums[n])
                if n > nextNum and sNums[n - 1] == sNums[n]:
                    continue
                backtrack(newSubset, n + 1, size)
                newSubset.pop()
            
        
        answer = []
        sNums = sorted(nums) # sort because backtrack doesn't work without a sorted list
        for i in range(len(nums) + 1):
            backtrack([], 0, i)
        return answer
    
s = Solution()
print(s.subsetsWithDup([1,2,2]))
print(s.subsetsWithDup([0]))
print(s.subsetsWithDup([1,1]))
print(s.subsetsWithDup([2,1,2,1,3]))