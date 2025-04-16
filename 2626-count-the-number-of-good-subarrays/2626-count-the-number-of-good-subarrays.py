class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        maps = {}
        cnt = left = 0
        for r in range(len(nums)):
            # check k ++ or not
            if nums[r] not in maps:
                maps[nums[r]] = 0
            k -= maps[nums[r]]
            maps[nums[r]] += 1
            while k <= 0:
                maps[nums[left]] -= 1
                k += maps[nums[left]]
                left += 1
            cnt += left
        return cnt
        # # n^2 to check how many good pairs
        # cnt = 0

        # for i in range(len(nums)):
        #     maps = defaultdict(int)
        #     pairs = 0
        #     for j in range(i, len(nums)):
        #         pairs += maps[nums[j]]
        #         maps[nums[j]] = maps[nums[j]] + 1
        #         if pairs >= k:
        #             cnt += 1
        # return cnt
