class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for n in nums:
            stack.append(n)
            while len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()
                stack[-1] *= 2

        # print(nums)
        return stack
