class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # using two pointer
        # l start from zero
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = 1_000_000_000 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += 2 ** (r - l)
                l += 1
        return res % mod
        # res = []
        # nums.sort()
        # def dfs(idx,tmp):
        #     res.append(tmp[:])
        #     for i in range(idx, len(nums)):
        #         tmp.append(nums[i])
        #         dfs(i + 1,tmp)
        #         tmp.pop()
        # dfs(0,[])
        # print(res)
        # cnt = 0
        # for sub_arr in res:
        #     if len(sub_arr) == 0:
        #         continue
        #     if sub_arr[0] + sub_arr[-1] <=target:
        #         cnt+=1
        # return cnt
