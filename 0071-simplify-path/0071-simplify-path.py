class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        # print(arr)
        res = []
        popCnt = 0
        while arr:
            cur = arr.pop()
            # print(cur)
            if cur == "" or cur == ".":
                continue
            elif cur == "..":
                popCnt += 1
            else:
                if popCnt > 0:
                    popCnt -= 1
                else:
                    res.append(cur)            
        ans = ""
        for i in range(len(res) - 1, -1, -1):
            ans = ans + "/" + res[i]
        return "/" if ans == "" else ans
