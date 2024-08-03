class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l,r = -1, len(citations)
        n = len(citations)
        while l+1!=r:
            mid = (l+r) //2

            if citations[mid] < n - mid:
                l = mid
            else:
                r = mid
        print(f"{l}, {r}")
        return n-r
