class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        # l = 1
        # r = 8
        # total = 7
        # l_h = 8
        # r_h = 7
        # cur = 7*7
        # res = 49
        
        while l < r:
            total_len = r - l
            cur = min(height[l], height[r]) * total_len
            res = max(res, cur)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
