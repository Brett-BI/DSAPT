class Solution:
    def isPalindrome(self, s: str) -> bool:
        l: int = 0
        r: int = len(s) - 1
        isPalindromeAnswer = True

        while l <= r:
            if s[l].isalnum() == False:
                l += 1
                continue

            if s[r].isalnum() == False:
                r -= 1
                continue

            if s[l].isalnum() and s[r].isalnum:
                if str.lower(s[l]) != str.lower(s[r]):
                    isPalindromeAnswer = False
                    break
            
            l += 1
            r -= 1

        return isPalindromeAnswer
    
    # T: O(N)
    # S: O(1) because it's constant?
    

s = Solution()
print(s.isPalindrome(" "))
print(s.isPalindrome("race a car"))
print(s.isPalindrome("A man, a plan, a canal: Panama"))