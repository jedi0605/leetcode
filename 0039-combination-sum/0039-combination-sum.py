class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        tmp_arr = []

        def dfs(idx, tmp_arr):
            s = sum(tmp_arr)
            if s > target:
                return
            if s == target:
                res.append(tmp_arr[:])
                return
            if idx == len(candidates):
                return
            # for i in range(len(candidates)):
            tmp_arr.append(candidates[idx])
            dfs(idx, tmp_arr)
            tmp_arr.pop()
            dfs(idx + 1, tmp_arr)

        dfs(0, tmp_arr)
        return res
