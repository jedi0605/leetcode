class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        numToListOfindices = defaultdict(list)

        for i, num in enumerate(nums):
            numToListOfindices[num].append(i)
        res = []
        for q in queries:
            arr = numToListOfindices[nums[q]]
            if len(arr) == 1:
                res.append(-1)
                continue
            idx = bisect_left(arr, q)
            min_dist = float("inf")
            # Only need to compare pre, next
            if idx == 0:
                min_dist = min(arr[idx + 1] - arr[idx], n - arr[-1] + arr[idx])
            elif idx == len(arr) - 1:
                min_dist = min(arr[idx] - arr[idx - 1], n - arr[idx] + arr[0])
            else:
                min_dist = min(arr[idx + 1] - arr[idx], arr[idx] - arr[idx - 1])
            res.append(min_dist)            

        return res
