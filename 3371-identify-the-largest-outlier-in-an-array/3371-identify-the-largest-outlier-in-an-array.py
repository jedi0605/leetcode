class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        cnt = Counter(nums)
        res = -inf
        # 2S + X = total
        for i in range(len(nums)): # loop S
            cnt[nums[i]] -=1
            target = total - 2 * nums[i]
            if cnt[target] > 0:
                res = max(res,target)
            cnt[nums[i]] +=1
        return res
            
            


            