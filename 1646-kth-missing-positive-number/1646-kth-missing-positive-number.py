class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        maps = set(arr)
        miss = 0
        for i in range(1,2002):
            if i not in maps:
                miss+=1
                if miss == k:
                    return i
        return -1