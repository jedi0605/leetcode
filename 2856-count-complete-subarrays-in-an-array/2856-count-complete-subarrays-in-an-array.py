class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        target_len = len(set(nums))
        cnt = Counter() # current sub arr
        right_pointer = 0

        for l in range(len(nums)):
            while right_pointer<len(nums) and len(cnt)< target_len:
                cnt[nums[right_pointer]]+=1
                right_pointer+=1
            
            if len(cnt) == target_len:
                res += len(nums) - right_pointer +1
            cnt[nums[l]]-=1
            if cnt[nums[l]] == 0:
                del cnt[nums[l]]
        return res
        
            