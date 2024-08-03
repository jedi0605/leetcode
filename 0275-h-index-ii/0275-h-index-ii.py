class Solution:
    def hIndex(self, citations: List[int]) -> int:

        hIdx = 0
        for i in range(len(citations)-1, -1, -1):
            if citations[i] > hIdx:
                hIdx += 1
        return hIdx