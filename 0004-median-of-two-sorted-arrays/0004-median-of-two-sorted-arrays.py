class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        l, r = 0, len(A) - 1
        while True:
            mid1 = (l + r) // 2  # A
            mid2 = half - mid1 - 2  # B
            Aleft = A[mid1] if mid1 >= 0 else float("-inf")
            Aright = A[mid1 + 1] if (mid1 + 1) < len(A) else float("inf")
            Bleft = B[mid2] if mid2 >= 0 else float("-inf")
            Bright = B[mid2 + 1] if (mid2 + 1) < len(B) else float("inf")
            if Aright >= Bleft and Bright >= Aleft:  # found ans
                print(f"{Aleft},{Aright}:{Bleft},{Bright}")
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = mid1 - 1
            else:
                l = mid1 + 1

        # brute force
        # tmp = nums1 + nums2
        # tmp.sort()
        # if len(tmp) % 2 == 0:
        #     mid = len(tmp) // 2
        #     res = (tmp[mid] + tmp[mid - 1]) / 2
        #     return res
        # else:
        #     return tmp[len(tmp) // 2]
