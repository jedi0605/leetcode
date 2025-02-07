class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur = []
        res = []

        def backtracking(idx):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(idx, len(nums)):
                if nums[i] not in cur:
                    cur.append(nums[i])
                    backtracking(idx)
                    cur.pop()

        backtracking(0)
        return res
