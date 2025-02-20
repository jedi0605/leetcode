class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # BF, list all combinations??
        length = len(nums[0])
        comb = []
        tmp = []
        # "1" , "0"
        # i = 0
        # tmp = [1]
        def dfs(i):
            if len(tmp) == length:
                comb.append("".join(tmp[:]))
                return
            tmp.append("0")
            dfs(i + 1)
            tmp.pop()
            tmp.append("1")
            dfs(i + 1)
            tmp.pop()

        dfs(0)
        numSet = set(nums)
        for s in comb:
            if s not in numSet:
                return s
        