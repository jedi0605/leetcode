class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = 0, 0
        zero1, zero2 = 0, 0
        for n in nums1:
            if n == 0:
                zero1 += 1
                sum1 += 1
            else:
                sum1 += n
        for n in nums2:
            if n == 0:
                zero2 += 1
                sum2 += 1
            else:
                sum2 += n
        if zero1 == 0 and sum1 < sum2:
            return -1
        if zero2 == 0 and sum2 < sum1:
            return -1
        return max(sum1, sum2)
