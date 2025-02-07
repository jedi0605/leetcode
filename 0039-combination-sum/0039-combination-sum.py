class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curArr = []

        def backtracking(curSum, idx):
            if curSum > target or idx == len(candidates):
                return
            if curSum == target:
                res.append(curArr[:])
                return

            curArr.append(candidates[idx])
            backtracking(curSum + candidates[idx], idx)
            curArr.pop()
            backtracking( curSum, idx + 1)

        backtracking(0, 0)
        return res
