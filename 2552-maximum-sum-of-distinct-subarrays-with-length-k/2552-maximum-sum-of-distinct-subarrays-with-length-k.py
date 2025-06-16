class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        init_arr = nums[:k]
        init_sum = sum(init_arr)
        dis_set = Counter(init_arr)
        max_sum = 0
        if len(dis_set) == k:
            max_sum = init_sum
        print(max_sum)
        for i in range(k, len(nums)):
            pre_num = nums[i - k]
            init_sum -= pre_num
            dis_set[pre_num] -= 1

            if dis_set[pre_num] == 0:
                del dis_set[pre_num]

            init_sum += nums[i]
            dis_set[nums[i]] += 1
            if len(dis_set) == k:
                max_sum = max(max_sum, init_sum)
        return max_sum
