class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        res = []
        for i in range(len( nums)):
            complet = target - nums[i]
            if  complet in dic:
                return [dic[complet],i]
            dic[nums[i]] = i
        print(dic)
        return []
