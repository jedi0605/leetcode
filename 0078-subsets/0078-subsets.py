class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

        def dfs(i):
            if i > len(nums) - 1:
                res.append(sub[:])
                return
            sub.append(nums[i])
            dfs(i + 1)
            sub.pop()
            dfs(i + 1)

        dfs(0)
        return res
