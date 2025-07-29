class Solution:
    def removeStars(self, s: str) -> str:
        print(s)
        stk = []

        for i in range(len(s)):
            if s[i] == "*":
                stk.pop()
            else:
                stk.append(s[i])

        print(stk)

        return "".join(stk)
    
s = Solution()
print(s.removeStars("leet**cod*e"))