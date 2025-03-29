class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Map = {val: idx for idx, val in enumerate(nums1)}
        right_bound = [-1] * len(nums2)
        res = [-1] * len(nums1)
        stack = []
        for idx, val in enumerate(nums2):
            while stack and nums2[stack[-1]] < val:
                g_idx = stack.pop()
                right_bound[g_idx] = val
                if nums2[g_idx] in nums1Map:
                    res[nums1Map[nums2[g_idx]]] = val
            stack.append(idx)
        return res
