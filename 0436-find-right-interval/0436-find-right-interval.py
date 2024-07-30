class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def bSearch(arr, target):
            l, r = -1, len(arr)
            while l + 1 != r:
                mid = (l + r) // 2
                if arr[mid][0] < target:
                    l = mid
                else:
                    r = mid
            return r if r != len(arr) else -1

        mapping = {}  # start not duplicate
        for i in range(len(intervals)):
            mapping[intervals[i][0]] = i
        intervals.sort()
        res = [-1] * len(intervals)

        for i in range(len(intervals)):
            right_idx = bSearch(intervals, intervals[i][1])  # closest right val, not idx
            print(f"{intervals[i][1]}. res {right_idx}")

            if right_idx != -1:
                res[mapping[intervals[i][0]]] = mapping[intervals[right_idx][0]]
        return res
