class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_h = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if sort_h[i]!=heights[i]:
                res+=1
        return res