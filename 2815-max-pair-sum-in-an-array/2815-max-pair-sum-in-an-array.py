class Solution:
    def maxSum(self, nums: List[int]) -> int:
        large = []

        for n in nums:
            max_digit = max(int(d) for d in str(n))
            large.append(max_digit)
        print(large)

        dic = defaultdict(list)
        for i in range(len(large)):
            dic[large[i]].append(nums[i])
        maxS = -1
        for key,val in dic.items():
            val.sort()
            if len(val) >1:
                maxS = max(maxS, val[-1]+val[-2])
        return maxS
