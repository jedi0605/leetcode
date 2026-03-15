class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        ans = comb(len(nums), 2)  # total pair
        print(ans)
        dic = defaultdict(int)
        for i, val in enumerate(nums):
            ans = ans - dic[i - val]
            dic[i - val] += 1

        return ans
