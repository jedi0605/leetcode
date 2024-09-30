class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def work_chunk(total_sum):
            total = 0
            chunk = 0
            for n in nums:
                total += n
                if total > total_sum:
                    total = n
                    chunk += 1
            return chunk + 1

        l, r = max(nums), sum(nums)

        while l < r:
            mid = (l + r) // 2
            if work_chunk(mid) > k:
                l = mid+1
            else:
                r = mid
        return r

        # res = []
        # def dfs(idx, tmpArr, remain):
        #     if remain == 0:
        #         if idx == len(nums):
        #             res.append(tmpArr[:])
        #         return

        #     for i in range(idx, len(nums)):
        #         tmpArr.append(nums[idx : i + 1])
        #         dfs(i + 1, tmpArr, remain - 1)
        #         tmpArr.pop()

        # dfs(0, [], k)
        # min_split = float("inf")
        # for r in res:
        #     local_max = float("-inf")
        #     for local_val in r:
        #         local_max = max(local_max,sum(local_val))
        #     min_split = min(local_max,min_split)
        # return min_split
