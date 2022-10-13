class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        rec = {}
        for i,first_numb in enumerate(nums):
            diff = target - first_numb
            if diff in rec:
                return i,rec[diff]
            else:
                rec[first_numb] = i