import collections
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        d = collections.defaultdict(int)
        for idx,ele in enumerate(nums):
            if ele in d and idx - d[ele] <= k:
                return True
            d[ele] = idx

        return False

