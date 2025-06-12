class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = nums[:k]
        init_cnt = Counter(start)
        max_sum = 0
        curr_sum = sum(start)
        if len(init_cnt) == k:
            max_sum = max(max_sum, curr_sum)

        for i in range(k, len(nums)):
            pre_num = nums[i - k]
            curr_sum -= pre_num
            init_cnt[pre_num] -= 1
            if init_cnt[pre_num] == 0:
                del init_cnt[pre_num]

            cur_num = nums[i]
            init_cnt[cur_num] += 1
            curr_sum += cur_num
            if len(init_cnt) == k:
                max_sum = max(max_sum, curr_sum)
        return max_sum
