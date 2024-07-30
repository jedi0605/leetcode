class SnapshotArray:

    # def __init__(self, length: int):
    #     self.snaps = 0
    #     self.arr = []
    #     for i in range(length):
    #         self.arr.append([])

    # def set(self, index: int, val: int) -> None:
    #     self.arr[index].append([val, self.snaps])

    # def snap(self) -> int:
    #     self.snaps += 1
    #     return self.snaps - 1

    # def get(self, index: int, snap_id: int) -> int:
    #     values = self.arr[index]
    #     print(values)
    #     res = 0
    #     start, end = 0, len(values) - 1
    #     while start <= end:
    #         mid = (start + end) >> 1
    #         if values[mid][1] <= snap_id:
    #             res = values[mid][0]
    #             start = mid + 1
    #         else:
    #             end = mid - 1
    #     return res
    def __init__(self, length: int):
        self.snap_times = 0
        self.arr = []
        for i in range(length):
            self.arr.append([])

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snap_times, val])

    def snap(self) -> int:
        self.snap_times += 1
        return self.snap_times - 1

    def get(self, index: int, snap_id: int) -> int:
        def bSearch(arr, target):
            l, r = -1, len(arr)
            while l + 1 != r:
                mid = (l + r) // 2
                if arr[mid][0] <= target:
                    l = mid
                else:
                    r = mid
            return l

        datas = self.arr[index]
        idx = bSearch(datas, snap_id)
        return self.arr[index][idx][1] if idx != -1 else 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
