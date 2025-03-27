class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        def findDominate(arr: List[int]):
            cnt = Counter(arr)
            overHalf = len(arr) // 2
            for c in cnt.keys():
                if cnt[c] > overHalf:
                    return c
            return -1

        # dominate = findDominate(nums)
        leftSide = defaultdict(int)
        rightSide = Counter(nums)
        for i in range(len(nums)):
            leftSide[nums[i]] += 1
            leftLen = i + 1

            rightSide[nums[i]] -= 1
            rightLen = len(nums) - leftLen
            if leftSide[nums[i]] * 2 > leftLen and rightSide[nums[i]] * 2 > rightLen:
                return i
        return -1
