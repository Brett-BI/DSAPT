from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        # opening: List[str] = []
        # closing: List[str] = []
        # opposite: List[str] = []

        # for c in s:
        #     if c == "(" or c == "{" or c == "[":
        #         opening.append(c)
        #     else:
        #         closing.append(c)

        # # figure out if they match
        # for c in closing:
        #     if c == ")":
        #         opposite.append("(")
            
        #     if c == "}":
        #         opposite.append("{")

        #     if c == "]":
        #         opposite.append("[")
            
        # if opening == opposite:
        #     return True
        # else:
        #     return False
        
        while len(s) > 0:
            print("For s: {}".format(s))
            lastOpenParen: int = 0
            for i in range(len(s)):
                if s[i] == "(" or s[i] == "{" or s[i] == "[":
                    lastOpenParen = i
            
            print(lastOpenParen)
            if lastOpenParen + 1 < len(s):
                parenPair = s[lastOpenParen] + s[lastOpenParen + 1]
                if parenPair == "()" or parenPair == "[]" or parenPair == "{}":
                    print("Removing: {}, {}".format(s[lastOpenParen], s[lastOpenParen + 1]))
                    s = s[:lastOpenParen] + s[lastOpenParen + 2:]
                else:
                    return False
            else: 
                return False

        return True
    
    # A stack is better; remember stack = first in, last out (FILO)
    # Add the character to the stack if it's an opener
    # Pop the topmost element from the stack if it's a matching closer
    # For each character in "([])":
    # Add "(" to stack. Stack is now ["("]
    # Add "[" to stack. Stack is now ["(", "["]
    # Found closer, remove topmost item from stack. Stack is now ["("]
    # Found closer, remove topmost item from stack. Stack is now []
    # After looking at all characters, if stack is empty, return True else return False

    # T: O(N^2)
    # S: O(N)




        
s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([])"))
print(s.isValid("["))
