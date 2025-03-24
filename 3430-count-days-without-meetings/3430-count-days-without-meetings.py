class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        # print(meetings)
        new_arr = []
        cur_arr = meetings[0]
        # do merge
        for i in range(len(meetings)):
            s,e = meetings[i][0],meetings[i][1]
            if s <= cur_arr[1]:
                cur_arr[1] = max(cur_arr[1],e)
            else:
                new_arr.append(cur_arr)
                cur_arr = meetings[i]
        new_arr.append(cur_arr)
        print(new_arr)
        res = 0
        for s,e in new_arr:
            res += (e-s+1)
        return days-res      




