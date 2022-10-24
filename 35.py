class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for idx,ele in enumerate(nums):
            if target <= ele:
                return idx
        else:
            return len(nums)