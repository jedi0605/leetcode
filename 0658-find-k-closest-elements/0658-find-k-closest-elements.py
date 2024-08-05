class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dis_idx = []

        for i in range(len(arr)):
            dis_idx.append( (abs(arr[i] - x),i ))

        print(dis_idx)
        sorted_data = sorted(dis_idx, key=lambda x: (x[0], x[1]))
        print(sorted_data)
        res = []
        for i in range(k):
            res.append(arr[  sorted_data[i][1]])
        res.sort()
        return res
