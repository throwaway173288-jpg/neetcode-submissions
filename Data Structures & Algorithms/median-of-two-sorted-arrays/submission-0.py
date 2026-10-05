class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=sorted(nums1+nums2)
        if len(res) % 2 == 0:
            return (res[len(res)//2] + res[(len(res)//2) - 1]) / 2
        else:
            return res[len(res) // 2]
            