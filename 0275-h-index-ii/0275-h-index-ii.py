class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1: return 0 if citations[0] == 0 else 1
        l,r = -1, len(citations)
        while l+1!=r:
            mid = (l+r) // 2
            if len(citations) - mid > citations[mid]:
                l = mid
            else:
                r= mid
        print(f"{l},{r}")
        return len(citations) - r
