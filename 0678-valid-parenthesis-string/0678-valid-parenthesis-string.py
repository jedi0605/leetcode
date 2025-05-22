class Solution:
    def checkValidString(self, s: str) -> bool:
        close_arr = []
        start_arr = []
        for i, cht in enumerate(s):
            if cht == "(":
                close_arr.append(i)
            if cht == "*":
                start_arr.append(i)
            if cht == ")":
                if len(close_arr) > 0:
                    close_arr.pop()
                elif len(start_arr) > 0:
                    start_arr.pop()
                else:
                    return False
        while close_arr and start_arr:
            if close_arr.pop() > start_arr.pop():
                return False
        return len(close_arr) == 0
