class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        num1_idx = 0
        num2_idx = 0
        res = []
        while num1_idx < len(nums1) and num2_idx < len(nums2):
            if nums1[num1_idx][0] == nums2[num2_idx][0]:
                # tmp = [nums1[num1_idx][0]] + nums1[num1_idx][1] + nums2[num2_idx][1]
                res.append(
                    [nums1[num1_idx][0], nums1[num1_idx][1] + nums2[num2_idx][1]]
                )
                num1_idx += 1
                num2_idx += 1
            elif nums1[num1_idx][0] < nums2[num2_idx][0]:
                res.append([nums1[num1_idx][0], nums1[num1_idx][1]])
                num1_idx += 1
            else:
                res.append([nums2[num2_idx][0], nums2[num2_idx][1]])
                num2_idx += 1
        if num1_idx != len(nums1):
            res = res + nums1[num1_idx:]
        if num2_idx != len(nums2):
            res = res + nums2[num2_idx:]
        return res
