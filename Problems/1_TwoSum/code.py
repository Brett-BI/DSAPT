from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # T: O(n^2) because there are two nested for loops
        # S: O(1) because there is no additional storage needed

    def twoSumHashMap(self, nums: List[int], target: int) -> List[int]:
        # key = number, value = index
        numHashMap: dict[int, List[int]] = {}

        # add to hashmap, technically constant time, I guess?
        for i in range(len(nums)):
            numHashMap[nums[i]] = i

        # pass through n, look for complement in hashmap
        for j in range(len(nums)):
            remainder = target - nums[j]
            if remainder in numHashMap and numHashMap[remainder] != j:
                return [j, numHashMap[remainder]]

        return []
    
        # T: O(n); technically O(2N) but the constant, 2, can be ignored because it is,
        # ultimately, negligible for large values of N
        # S: O(N) because we have one additional storage item of size N, the hashmap