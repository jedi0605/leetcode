class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        numToListOfindices = defaultdict(list)

        for i, num in enumerate(nums):
            numToListOfindices[num].append(i)
        print(numToListOfindices)

        for arr in numToListOfindices.values():
            m = len(arr)

            if len(arr) == 1:
                nums[arr[0]] = -1
                continue
            for i in range(m):
                curr_idx_val = arr[i]
                nex_same_idx = (i + 1) % m
                pre_same_idx = (i - 1) % m
                nex_same_idx_val = arr[nex_same_idx]
                nex_dist = min(
                    abs(nex_same_idx_val - curr_idx_val),
                    abs(n - curr_idx_val + nex_same_idx_val),
                )

                pre_same_idx_val = arr[pre_same_idx]
                pre_dist = min(
                    abs(curr_idx_val - pre_same_idx_val),
                    abs(n - pre_same_idx_val + curr_idx_val),
                )

                nums[arr[i]] = min(abs(nex_dist), abs(pre_dist))

        res = []
        for i in range(len(queries)):
            res.append(nums[queries[i]])
        return res
