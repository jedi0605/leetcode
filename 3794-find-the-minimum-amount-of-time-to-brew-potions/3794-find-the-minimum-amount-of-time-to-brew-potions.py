class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        last_finished = [0] * n

        for m in mana:
            # go -> to calutate
            sum_t = 0  #
            for x, last in zip(skill, last_finished):
                sum_t = max(last, sum_t) + x * m
            last_finished[-1] = sum_t
            # go <- to adjust time
            for i in range(n - 2, -1, -1):
                last_finished[i] = last_finished[i + 1] - skill[i + 1] * m
        return last_finished[-1]
