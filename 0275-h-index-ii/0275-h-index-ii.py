class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1: return 0 if citations[0] == 0 else 1
        h = 0
        citations.sort()
        for i in range(len(citations)-1,-1,-1):
            if citations[i] > h:
                h+=1
        return h