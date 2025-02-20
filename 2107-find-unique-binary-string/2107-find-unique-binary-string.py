class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums[0])
        numSet = set(nums)
        def generate(curr):
            if len(curr) == length:
                if curr not in numSet:
                    return curr
                return ""
            add_zero = generate(curr+"0")
            if add_zero:
                return add_zero
            return generate(curr+"1")
        return generate("")
        # # BF, list all combinations??
        # length = len(nums[0])
        # comb = []
        # tmp = []
        # def dfs(i):
        #     if len(tmp) == length:
        #         comb.append("".join(tmp[:]))
        #         return
        #     tmp.append("0")
        #     dfs(i + 1)
        #     tmp.pop()
        #     tmp.append("1")
        #     dfs(i + 1)
        #     tmp.pop()

        # dfs(0)
        # numSet = set(nums)
        # for s in comb:
        #     if s not in numSet:
        #         return s
