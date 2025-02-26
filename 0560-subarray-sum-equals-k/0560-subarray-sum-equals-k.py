class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # using prefix sum
        #
        total = 0
        res = 0
        maps = defaultdict(int)  # sum, cnt
        # 0, 1
        # 1, 1
        # n == 1, total = 1,  k - total == -1, lookup in dic
        # if not exist than update dic, else update res += dic[-1]
        maps[0] = 1
        for n in nums:
            total += n
            diff = total -k
            if diff in maps:
                res += maps[diff]
                maps[total] += 1
            else:
                maps[total] += 1
        return res
