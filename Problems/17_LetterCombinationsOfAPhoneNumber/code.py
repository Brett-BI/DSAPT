class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lettersDict: dict[int, List[str]] = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
        def backtrack(currentString, currentOptionList):
            # base case
            if len(currentString) == len(digits):
                # accounting for len(currentString) == 0
                if currentString:
                    answer.append("".join(currentString[:]))
                return

            # recurse
            # look at the current list of options
            for option in optionsList[currentOptionList]:
                currentString.append(option)
                # recurse and use the next list of options
                backtrack(currentString, currentOptionList + 1)
                currentString.pop()
        

        answer = []
        optionsList = []
        for d in digits:
            optionsList.append(lettersDict[d])
        backtrack([], 0)

        return answer
    
    # T: O(3 ^ n * 4 ^ m)