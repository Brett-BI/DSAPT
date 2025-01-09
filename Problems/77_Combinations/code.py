
from typing import List


class Solution():
    def combine(self, n, k):
        def backtrack(currentCombo: List[int], nextCharacter: int):
            # base case
            if len(currentCombo) == k:
                answer.append(currentCombo[:])
                return 
            
            # iterate through all possible candidates
            # use n+1 because the solution has to be inclusive of n
            # and the upper bound of range() is exclusive
            for i in range(nextCharacter, n + 1):
                # add candidate
                currentCombo.append(i)
                # recurse and increase the nextCharacter value so that the next 
                # for loop evaluates the lower bound of range() as i+1
                # this prevents repeat characters from ocurring
                backtrack(currentCombo, i + 1)
                # remove last character and try the next in the for loop
                currentCombo.pop()
        
        answer: List[int] = []
        backtrack([], 1)
        return answer
    
    # T: O(n! / ((k - 1)! * (n - k)!)) - this is in "n choose k" time complexity
    #   the n! makes sense but it's not whole picture: the dwindling number of candidate 
    #   values plays a factor. Probably best to just memorize this one. One more note: 
    #   this is the total number of recursive calls, essentially. If additional work 
    #   needed to be done on each recursive call that was in O(1) or O(k), the time 
    #   complexity would change.

s = Solution()
print(s.combine(4, 2))
print(s.combine(1, 1))
print(s.combine(4, 3))
print(s.combine(3, 3))


# NOTE: here is my original solution.
# This finds an answer but the lookup is too slow to pass
'''
# possible numbers to use in combo
        numbers: List[num] = []
        for i in range(1, n + 1):
            numbers.append(i)

        def backtrack(currentCombo: List[int], possibleValues: [int]):
            # base case
            if len(currentCombo) == k:
                # add to dict both ways for a quick lookup
                # comboHasBeenSeen: bool = False
                matches: int = 0
                for a in answer:
                    matches = 0
                    for c in currentCombo:
                        if c in a:
                            matches += 1
                            
                    if matches == k:
                        break

                if matches < k:
                    answer.append(currentCombo[:])

                return

            for v in possibleValues: 
                if v not in currentCombo:
                    currentCombo.append(v)
                    backtrack(currentCombo, possibleValues[1:])
                    currentCombo.pop()


        # loop? is recursion necessary?
        answerDict = {}
        answer: List[List[int]] = []
        backtrack([], numbers)

        return answer
'''