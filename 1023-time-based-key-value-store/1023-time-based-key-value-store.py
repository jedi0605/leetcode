class TimeMap:

    def __init__(self):
        self.key_str = defaultdict(list)
        self.key_time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_str[key].append(value)
        self.key_time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_str:
            return ""
        idx = bisect_right(self.key_time[key], timestamp)-1
        print(idx)
        if idx < 0:
            return ""
        return self.key_str[key][idx]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)