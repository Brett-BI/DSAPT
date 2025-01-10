class Solution():
    def subsets(self, nums): 
        # O(2 ^ n)
        def backtrack(currentCombo, lowerBound, size): 
            # base case
            if len(currentCombo) == size:
                answer.append(currentCombo[:])
                return
            
            # combination binomial coefficient
            for n in range(lowerBound, len(nums)):
                currentCombo.append(nums[n])
                backtrack(currentCombo, n + 1, size) 
                currentCombo.pop()

        answer = []
        itemsToChoose = 0
        while itemsToChoose <= len(nums): # O(n)
            backtrack([], 0, itemsToChoose)
            itemsToChoose += 1

        return answer
    
    # T: O(2 ^ n * n)
    # 2^n calls (math behind subsets, size 0 - k), binomial coefficient of combo problem, 
    # n calls for while loop
    # S: O(2^n * n) because you make the recursive call n times to build one subset, 
    # the currentCombo is, at most, of size n, and results are always of size 2^n. 
    # Technically O(2 ^ n * n + n) but remove the constant, n.
        

s = Solution()
print(s.subsets([1,2,3]))