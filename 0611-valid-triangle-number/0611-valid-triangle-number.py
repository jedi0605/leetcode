class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-1,-1,-1):
            l,r = 0 , i -1
            while l<r:
                if nums[l] + nums[r] > nums[i]:
                    res+=r-l
                    r-=1
                else:
                    l+=1
        return res


        # nums.sort()
        # res = 0
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j] > nums[k]:
        #                 res+=1
        # return res

        # nums.sort()  # Sort in ascending order
        # self.count = 0
        # n = len(nums)

        # def dfs(index, sides):
        #     print(sides)
        #     if len(sides) == 3:
        #         if sides[0] + sides[1] > sides[2]:
        #             self.count += 1
        #         return
            
        #     for i in range(index, n):
        #         sides.append(nums[i])
        #         dfs(i + 1, sides)
        #         sides.pop()

        # dfs(0, [])
        # return self.count

