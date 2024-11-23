class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # cnt = Counter(nums)
        # res = 0
        # max_cnt = 0
        # print(cnt)
        # for num, c in cnt.items():
        #     if c > max_cnt:
        #         max_cnt = c
        #         res = num
        # return res

        res = 0
        cnt = 0
        for n in nums:
            if cnt == 0:
                res = n
            if res == n:
                cnt+=1
            else:
                cnt -=1
        return res