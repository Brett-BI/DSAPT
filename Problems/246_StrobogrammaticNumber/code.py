class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammaticNumbers: dict[str, bool] = {
            "0": True,
            "1": True,
            "2": False,
            "3": False,
            "4": False,
            "5": False,
            "6": False,
            "7": False,
            "8": True,
            "9": False
        }
        l: int = 0
        r: int = len(num) - 1
        isStrobogrammatic: bool = True

        while l <= r:
            # numbers probably need to be the same?
            if num[l] == num[r] and strobogrammaticNumbers[num[l]] == True and strobogrammaticNumbers[num[r]] == True:
                isStrobogrammatic = True
            elif (num[l] == "6" and num[r] == "9") or (num[l] == "9" and num[r] == "6"):
                # covers the specific case of 69 or 96 because these aren't strobogrammatic 
                # on their own but they are when next to each other and in the center of 
                # the original string
                isStrobogrammatic = True
            else:
                isStrobogrammatic = False
                break
        
            l += 1
            r -= 1

        return isStrobogrammatic
    
    # T: O(N): .5 * N because I'm using two pointer, lookups are O(1)
    # S: O(1): space requirements are not dynamic
    
s = Solution()
print(s.isStrobogrammatic("69"))
print(s.isStrobogrammatic("88"))
print(s.isStrobogrammatic("962"))
print(s.isStrobogrammatic("10"))