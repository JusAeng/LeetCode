class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        c = len(nums1)+len(nums2)
        n = (c+1)//2
        nums1.append(1000001)
        nums2.append(1000001)
        for i in range(n):
            if nums1[0] < nums2[0] or not nums2:
                kick = nums1.pop(0)
            else:
                kick = nums2.pop(0)
        else:
            if c%2==0:
                return (kick + min(nums1[0],nums2[0]))/2
            else:
                return kick
       