class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        mod = 10 ** 9 + 7
        nums.sort()
        for i in range(len(nums)):
            if nums[i] + nums[i] > target:
                break
            sub_target = target - nums[i]
            idx = bisect_right(nums,sub_target) -1
            if idx < len(nums):
                res += 2 ** (idx - i)
        return res % mod

        # brute force. list all Sub Seq
        # res = []
        # nums.sort()
        # def dfs(start, curr_arr):
        #     if curr_arr:
        #         res.append(curr_arr[:])
            
        #     for i in range(start, len(nums)):
        #         curr_arr.append(nums[i])
        #         dfs(i + 1, curr_arr)
        #         curr_arr.pop()

        # dfs(0, [])
        # print(res)
        # ans = 0
        # for r in res:
        #     if r[0]+r[-1] <=target:
        #         ans+=1        
        # return ans