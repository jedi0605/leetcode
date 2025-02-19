class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        # [1,2]
        # i = 2
        # res = [[1,2] , [1], [2],[]]
        # tmp = []
        def dfs(i):
            if i == len(nums):
                res.append(tmp.copy())
                return
            tmp.append(nums[i])
            dfs(i+1)
            tmp.pop()
            dfs(i+1)
        dfs(0)
        return res