class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hash_set = set(nums)
        res = 0
        for h in hash_set:
            if h < k:
                return -1
            if h > k:
                res+=1
        return res