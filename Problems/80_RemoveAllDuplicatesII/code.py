class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i: int = 2
        insert: int = 2

        # Need to preserve order
        # insert holds the index from the left
        # for insertion in order
        while i <= len(nums) - 1:
            if nums[i] != nums[insert - 2]:
                nums[insert] = nums[i]

                insert += 1
            
            i += 1
        return insert
        