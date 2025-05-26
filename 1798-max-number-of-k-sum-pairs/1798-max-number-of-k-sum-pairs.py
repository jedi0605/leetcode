class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        operation = 0

        # 1:1
        # 3:1
        # 4:1
        # cur_num:3
        # target_num:3
        for cur_num in nums:
            target_num = k - cur_num

            if target_num == cur_num: #edge_case -2                
                if cnt[target_num] >=2:
                    operation+=1
                    cnt[target_num]-=2
            else: # each num -1
                if cnt[target_num] >0 and cnt[cur_num] >0:
                    operation+=1
                    cnt[target_num] -=1
                    cnt[cur_num]-=1
        return operation

