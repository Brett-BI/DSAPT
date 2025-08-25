from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        doubleDigitTotal = 0
        singleDigitTotal = 0

        for n in nums:
            if n > 9:
                doubleDigitTotal += n
            else:
                singleDigitTotal += n
        
        return (doubleDigitTotal > singleDigitTotal) or (singleDigitTotal > doubleDigitTotal)
    
s = Solution()
print(s.canAliceWin([1,2,3,4,10])) # false
print(s.canAliceWin([1,2,3,4,5,14])) # true
print(s.canAliceWin([5,5,5,25])) # true