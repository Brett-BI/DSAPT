from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        strobogrammaticNumbers: List[int] = [0, 1, 6, 8, 9]

        def isStrobogrammatic(numString: List[int]) -> bool:
            strobogrammaticNumbersDict: dict[int, bool] = {
                1: True,
                8: True
            }
            l: int = 0
            r: int = len(numString) - 1
            isStrobogrammaticNumber = True

            while l <= r:
                if numString[l] == numString[r] and numString[l] in strobogrammaticNumbersDict and numString[r] in strobogrammaticNumbersDict:
                    isStrobogrammaticNumber = True
                elif (numString[l] == 6 and numString[r] == 9) or (numString[l] == 9 and numString[r] == 6):
                    isStrobogrammaticNumber = True
                elif numString[l] == 0 and numString[r] == 0:
                    if l != r and len(numString) <= 2:
                        isStrobogrammaticNumber = False
                        break
                else: 
                    isStrobogrammaticNumber = False
                    break

                l += 1
                r -= 1
            
            return isStrobogrammaticNumber

        def backtrack(currentString):
            if len(currentString) == n:
                # print("Trying: ")
                # print(currentString[:])
                if isStrobogrammatic(currentString):
                    r = ""
                    for c in currentString:
                        r += str(c)
                    answer.append(r)
                return
            
            for num in strobogrammaticNumbers:
                if num == 0 and len(currentString) == 0 and n > 1:
                    continue
                else:
                    currentString.append(num)
                    backtrack(currentString)
                    currentString.pop()


        answer = []
        backtrack([])

        return answer
    
s = Solution()
print(s.findStrobogrammatic(2))
print(s.findStrobogrammatic(1))
print(s.findStrobogrammatic(4))