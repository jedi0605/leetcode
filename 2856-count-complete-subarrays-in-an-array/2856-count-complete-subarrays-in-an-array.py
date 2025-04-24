class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target_set = set(nums)
        target_set_len = len(target_set)
        res = 0
        for i in range(len(nums)):
            # build sub arr
            cur_set = set()
            for j in range(i,len(nums)):
                cur_set.add(nums[j])
                
                if len(cur_set) == target_set_len:
                    print(j)
                    res+= len(nums) - j
                    break
        return res

            