class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tmp = nums1 + nums2
        tmp.sort()
        if len(tmp) % 2 == 0:
            mid = len(tmp) // 2
            res = (tmp[mid] + tmp[mid - 1]) / 2
            return res
        else:
            return tmp[len(tmp) // 2]
        print(tmp)
        return 0
