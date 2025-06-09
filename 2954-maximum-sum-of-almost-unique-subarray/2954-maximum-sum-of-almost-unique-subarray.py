class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        init_arr = nums[:k]
        init_sum = sum(init_arr)
        cnt = Counter(init_arr)

        max_sum = init_sum if len(cnt) >= m else 0
        for i in range(k,len(nums)):
            curr = nums[i]
            remove_target = nums[i-k]
            cnt[remove_target] -= 1
            init_sum -= remove_target
            if cnt[remove_target] == 0:
                del cnt[remove_target]
            cnt[curr]+=1
            init_sum+=curr
            if len(cnt) >=m:
                max_sum = max(max_sum,init_sum)
        return max_sum
            