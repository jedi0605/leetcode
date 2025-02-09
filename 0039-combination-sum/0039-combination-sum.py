class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur = []
        res = []

        def backtracking(target, idx):
            if target < 0 or idx >= len(candidates):
                return
            if target == 0:
                res.append(cur.copy())
                return            
            cur.append(candidates[idx])
            backtracking(target - candidates[idx], idx)
            cur.pop()
            backtracking(target , idx + 1)
        backtracking(target, 0)
        return res