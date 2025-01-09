class Solution():
    def subsets(self, nums): 
        def backtrack(currentCombo, lowerBound, size): 
            # base case
            if len(currentCombo) == size:
                answer.append(currentCombo[:])
                return
            
            for n in range(lowerBound, len(nums)):
                currentCombo.append(nums[n])
                backtrack(currentCombo, n + 1, size) # not lowerbound + 1... dumbass.
                currentCombo.pop()

            

        answer = []
        itemsToChoose = 0
        while itemsToChoose <= len(nums):
            backtrack([], 0, itemsToChoose)
            itemsToChoose += 1

        return answer
        

s = Solution()
print(s.subsets([1,2,3]))