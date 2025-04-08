class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
                
        def check_dist(arr)-> bool:
            dist = set(arr)
            return len(dist) == len(arr)            
        
        if check_dist(nums):
            return 0
        res = 0
        while check_dist(nums) == False:
            if len(nums) > 3:
                nums = nums[3:]
            else:
                res+=1
                break
            res+=1
        return res