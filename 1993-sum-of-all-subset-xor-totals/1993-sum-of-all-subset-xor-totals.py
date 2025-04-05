class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor_total(arr: List[int]):
            res = 0
            for a in arr:
                res = xor(a, res)
            return res

        sub_set = []
        tmp = []

        def backtracking(idx):
            if idx == len(nums):
                sub_set.append(tmp.copy())
                return
            if idx > len(nums):
                return
            tmp.append(nums[idx])
            backtracking(idx + 1)
            tmp.pop()
            backtracking(idx + 1)
            return

        backtracking(0)
        res = 0
        for arr in sub_set:
            res += xor_total(arr)
        return res
