class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def work_chuck(chuck):
            total = 0
            cur = 0
            for n in nums:
                cur += n
                if cur > chuck:
                    total+=1
                    cur = n
            return total+1
        print( work_chuck(18))
        l,r = max(nums), sum(nums)
        while l<r:
            mid = (l+r) //2
            if work_chuck(mid) > k:
                l = mid+1
            else:
                r= mid
        return l
        # res = []
        
        # def dfs(tmpArr,idx,remain):
        #     if remain == 0:
        #         if idx == len(nums):
        #             res.append(tmpArr[:])
        #         return
        #     for i in range(idx,len(nums)):
        #         tmpArr.append(nums[idx:i+1])
        #         dfs(tmpArr, i+1 ,remain -1)
        #         tmpArr.pop()
        # dfs([],0,k)
        # min_res = float("inf")
        # for a in res:
        #     local_max = 0
        #     for values in a:
        #         local_max = max(local_max,sum(values))
        #     min_res = min(min_res,local_max)

        # return min_res