class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def work(total_sum):
            total = 0
            chunk = 0
            for n in nums:
                total+=n
                if total > total_sum:
                    chunk += 1
                    total = n
            return chunk + 1

        print(work(18))
        print(work(17))
        l = len(nums)
        r = sum(nums)
        ans = 0
        while l < r:
            mid = (l + r) // 2
            # mid = 10, => [7,2,5][10][8] (work)
            if work(mid)>k:
                l = mid + 1
            else:                
                r = mid
        return r
        # res = []
        # def dfs(idx, remain, cur_arr):
        #     if remain == 0:
        #         if idx == len(nums):
        #             res.append(cur_arr[:])
        #         return
        #     for i in range(idx, len(nums)):
        #         cur_arr.append(nums[idx : i + 1])
        #         dfs(i + 1, remain - 1, cur_arr)
        #         cur_arr.pop()

        # dfs(0, k, [])
        # min_sum = float("inf")
        # for arr in res:
        #     local_max = float("-inf")
        #     for a in arr:
        #         local_max = max(sum(a),local_max)
        #     min_sum = min(min_sum,local_max)

        # return min_sum
