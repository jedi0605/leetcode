class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        res = 0
        max_cnt = 0
        print(cnt)
        for num, c in cnt.items():
            if c > max_cnt:
                max_cnt = c
                res = num
        return res