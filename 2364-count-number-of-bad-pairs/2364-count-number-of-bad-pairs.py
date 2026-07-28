class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        res = 0
        total_pair = math.comb(len(nums),2)        
        # we want to get good?
        # nums[i] - i == nums[j] - j
        #[4-0, 1-1, 3-2,3-3]
        #[4,0,1,0]
        freq = defaultdict(int)
        good_pair = 0
        for i in range(len(nums)):
            tmp_num = nums[i] - i
            good_pair += freq[tmp_num]
            freq[tmp_num]+=1

        return total_pair - good_pair

        # [1,2,3,4,5]
        # [1-0,2-1,3-2,4-3,5-4]
        # [1,1,1,1,1]