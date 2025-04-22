class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        org_arr = [0] * (len(differences)+1)
        for i in range(len(differences)):
            org_arr[i+1] = differences[i]+org_arr[i]
        min_arr = min(org_arr)
        max_arr = max(org_arr)
        diff = max_arr - min_arr
        range_diff = upper - lower
        if diff > range_diff:
            return 0
        return range_diff-diff +1