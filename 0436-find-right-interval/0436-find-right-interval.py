class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        idx_map = {}
        sort_arr = []
        for i in range(len(intervals)):
            idx_map[intervals[i][0]] = i # {val, idx}
            sort_arr.append(intervals[i][0])
        sort_arr.sort()
        print(idx_map)
        print(sort_arr)
        res = []
        for i in range(len(intervals)):
            index = bisect_left(sort_arr, intervals[i][1])
            if index == len(sort_arr):
                res.append(-1)
            else:
                index_val = sort_arr[index]
                res.append(idx_map[index_val])
        return res
        