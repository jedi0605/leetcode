class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        diff_nums = []
        for i in range(1, len(weights)):
            diff_nums.append(abs(weights[i - 1] + weights[i]))
        print(diff_nums)
        diff_nums.sort()
        k = k - 1  #
        print(diff_nums[-k:])
        max_wei = sum(diff_nums[-k:])
        min_wei = sum(diff_nums[:k])
        return max_wei - min_wei
