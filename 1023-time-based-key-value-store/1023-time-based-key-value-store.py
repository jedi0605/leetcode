class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = [(value,timestamp)]
        else:
            self.mapping[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ""
        def bSearch(arr, target):
            l ,r = -1 , len(arr)
            while l+1!=r:
                mid = (l+r)//2
                if arr[mid][1] <= target:
                    l = mid
                else:
                    r = mid
            return l
        idx = bSearch(self.mapping[key], timestamp)
        
        return self.mapping[key][idx][0] if idx != -1 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)