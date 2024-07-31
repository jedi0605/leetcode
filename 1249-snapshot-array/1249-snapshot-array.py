class SnapshotArray:

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
        def b_search(search_arr, target):
            l, r = -1, len(search_arr)
            while l + 1 != r:
                mid = (l + r) // 2
                if search_arr[mid][0] <= target:
                    l = mid
                else:
                    r = mid
            return l if l != -1 else -1
        search_arr = self.arr[index]
        idx = b_search(search_arr, snap_id)
        
        return search_arr[idx][1] if idx != -1 else 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
