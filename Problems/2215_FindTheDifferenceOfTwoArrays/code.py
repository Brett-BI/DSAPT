from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        '''
        Time: O(N * M)
        Space: O(N + M)
        '''
        in1: set[int] = set([])
        in2: set[int] = set([])

        for n in nums1:
            if n not in nums2:
                in1.add(n)

        for n in nums2:
            if n not in nums1:
                in2.add(n)

        return [list(in1), list(in2)]


    def findDifferenceFast(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        '''
        Time: O(N + M)
        Space: O(N + M)
        '''
        # convert lists to sets to go from lookup O(n) -> O(1)
        n1s: set[int] = set(nums1)
        n2s: set[int] = set(nums2)

        in1 = []
        in2 = []

        for n in n1s:
            if n not in n2s: 
                in1.append(n)

        for n in n2s:
            if n not in n1s:
                in2.append(n)
        
        return [in1, in2]
    

s = Solution()
print(s.findDifference([1,2,3], [2,4,6]))