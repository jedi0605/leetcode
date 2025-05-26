class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_res = -1

        def sumDigit(num : int)->int:
            s = str(num)
            res = 0
            for c in s:
                res +=int(c)
            return res
        digit_maps = defaultdict(int) # store digi, max num

        for n in nums:
            digit = sumDigit(n)
            if digit in digit_maps:
                max_res = max(max_res, digit_maps[digit] + n)
                digit_maps[digit] = max(digit_maps[digit],n)
            else:
                digit_maps[digit] = n

        return max_res
        