class TimeMap:

    def __init__(self):
        self.maps = {}
        self.saveVal = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.maps:
            self.maps[key] = [timestamp]
            self.saveVal[key] = [value]
        else:
            self.maps[key].append(timestamp)
            self.saveVal[key].append(value)            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.maps:
            return ""
        idx = bisect_right(self.maps[key], timestamp) - 1      
        if idx <0 :
            return ""
        return self.saveVal[key][idx]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)