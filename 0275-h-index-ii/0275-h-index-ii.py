class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations[-1] == 0:
            return 0
        l, r = -1, len(citations)
        n = len(citations)
        while l + 1 != r:
            mid = (l + r) // 2
            if n - mid > citations[mid]:
                l = mid
            else:
                r = mid
        print(f"{l},{r}")
        return n-r

        # brute force
        # hIdx = 0
        # for i in range(len(citations)-1, -1, -1):
        #     if citations[i] > hIdx:
        #         hIdx += 1
        # return hIdx
