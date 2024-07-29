class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        mapping={}
        for idx, interval in enumerate(intervals):
            mapping[interval[0]]=idx
        print(mapping)
        intervals.sort()
        n=len(intervals)
        def binary_search(intervals, target):
            left=0
            right=n-1
            while left <= right:
                mid = left + (right-left)//2
                if intervals[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == n:
                return -1
            else:
                return left
        res = [-1] * n
        for i in range(n):
            idx2 = binary_search(intervals, intervals[i][1])
            if idx2 != -1:
                res[mapping[intervals[i][0]]] = mapping[intervals[idx2][0]]
            # else:
            #     res[mapping[intervals[i][0]]] = -1
        return res
# class Solution:
#     def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
#         # find greater than target's idx
#         def bSearch(intervals, target):
#             l, r = -1, len(intervals)
#             while l + 1 != r:
#                 mid = (l + r) // 2
#                 if intervals[mid][0] <= target:
#                     l = mid
#                 else:
#                     r = mid
#             return r if r != len(intervals) else -1

#         if len(intervals) == 1:
#             return [-1]
#         mapping = {}
#         for i in range(len(intervals)):
#             mapping[intervals[i][0]] = i
#         print(mapping)
#         intervals.sort()
#         print(intervals)
#         res = [-1] * len(intervals)
#         for i in range(len(intervals)):
#             idx = bSearch(intervals,intervals[i][1])
#             if idx!=-1:
#                 res[ intervals[i][0]  ] = mapping[intervals[idx][0]]
            
#         return res