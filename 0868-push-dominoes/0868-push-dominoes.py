class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        q = deque()
        for i, c in enumerate(dom):
            if c !=".":
                q.append((i,c))
        print(q)
        while q:
            idx, c = q.popleft()
            if c == "L" and idx>0 and dom[idx-1] == ".":
                dom[idx-1] = "L"
                q.append((idx-1,"L"))
            if c == "R":
                if idx + 1< len(dom) and dom[idx+1] == ".":
                    if idx+2<len(dom) and dom[idx+2] == "L":
                        q.popleft()
                    else:
                        dom[idx+1] = "R"
                        q.append((idx+1,"R"))
        return "".join(dom)


        