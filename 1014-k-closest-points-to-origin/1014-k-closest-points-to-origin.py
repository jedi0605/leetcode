class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dis = (x**2) + (y**2)
            minHeap.append( [dis, x, y])
        heapify(minHeap)
        res = []
        for i in range(k):
            d, x, y = heappop(minHeap)
            res.append([x, y])
        return res
