class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l != r:
            # cauculate
            if height[l] > height[r]:
                res = max(res, height[r] * (r - l))
                r-=1
            else:
                res = max(res, height[l] * (r - l))
                l+=1
        return res
