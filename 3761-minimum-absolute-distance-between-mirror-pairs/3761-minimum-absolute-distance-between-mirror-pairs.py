class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        def reverse(num) -> int:
            strings = str(num)[::-1]
            buildS = []
            for i in range(len(strings)):
                if strings[i] != "0":
                    buildS = strings[i:]
                    break
            return int("".join(buildS))

        dic = defaultdict(int)  # store reverse and max idx
        res = inf
        for idx, val in enumerate(nums):
            if val in dic:
                
                res = min(res, idx - dic[val])
            rInt = reverse(val)
            dic[rInt] = max(dic[rInt], idx)
        print(dic)
        return -1 if res == inf else res
