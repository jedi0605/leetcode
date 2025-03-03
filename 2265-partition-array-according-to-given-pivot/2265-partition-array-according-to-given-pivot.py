class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        leftA = []
        rightA = []
        pivotA = []
        for n in nums:
            if n == pivot:
                pivotA.append(n)
            elif n < pivot:
                leftA.append(n)
            else:
                rightA.append(n)
        return leftA+pivotA+rightA