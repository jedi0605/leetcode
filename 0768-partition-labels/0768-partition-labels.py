class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maps = {}
        for idx, val in enumerate(s):
            if val not in maps:
                maps[val] = [idx, idx]
            else:
                maps[val][1] = idx
        res_arr = []
        interval = [ maps[s[0]][0],maps[s[0]][1]]
        for idx, val in enumerate(s):
            char_interval = [ maps[val][0],maps[val][1]]
            if char_interval[0]<= interval[1]: # overlap
                interval[1] = max(interval[1],char_interval[1])
            else: # no overlap
                res_arr.append(interval.copy())
                interval = char_interval
        res_arr.append(interval)
        res = []
        for arr in res_arr:
            res.append(arr[1]-arr[0]+1)
        return res

