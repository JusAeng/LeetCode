class Solution:
    def findErrorNums(self, nums):
        s_num = set(nums)
        b = set(range(1,len(nums)+1)) - s_num
        a = sum(nums) - sum(s_num)
        return a , b.pop()