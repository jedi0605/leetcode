class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        l, r = 0, len(queries)

        def fit(k):
            sweep = [0] * (len(nums) + 1)
            for q in range(k):
                l_idx, r_idx, val = queries[q][0], queries[q][1], queries[q][2]
                sweep[l_idx] += val
                sweep[r_idx + 1] -= val
            # check prefix
            total = 0
            for i in range(len(nums)):
                total += sweep[i]
                if total < nums[i]:
                    return False
            return True

        if fit(r) == False:
            return -1

        while l <= r:  # B search....
            mid = (l + r) // 2
            if fit(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
