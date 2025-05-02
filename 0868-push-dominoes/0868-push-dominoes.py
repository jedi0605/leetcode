class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        do_arr = list(dominoes)
        mark = [False] * len(dominoes)
        pairs = []
        # find R-L pair
        tmp = []
        for idx, c in enumerate(dominoes):
            if c == "L" or c == "R":
                tmp.append((c, idx))

        for i in range(len(tmp) - 1):
            c, idx = tmp[i][0], tmp[i][1]
            if c == "R" and tmp[i + 1][0] == "L":
                pairs.append((idx, tmp[i + 1][1]))
        print(pairs)
        # do R-L pair also mark as done
        for l_side, r_side in pairs:
            while l_side <= r_side:
                if l_side == r_side:
                    mark[r_side] = True
                    break
                mark[l_side] = True
                mark[r_side] = True
                do_arr[l_side] = "R"
                do_arr[r_side] = "L"
                l_side += 1
                r_side -= 1
        # print(do_arr)
        # print(mark)
        # take care of right to left
        for i in range(len(do_arr) - 1, -1, -1):
            if (
                do_arr[i] == "L" and mark[i] == False
            ):  # go right until do_arr == True or end of arr
                while i > -1 and mark[i] == False:
                    mark[i] = True
                    do_arr[i] = "L"
                    i -= 1
        # take care of left to right
        for i in range(len(do_arr)):
            if (
                do_arr[i] == "R" and mark[i] == False
            ):  # go right until do_arr == True or end of arr
                while i < len(do_arr) and mark[i] == False:
                    mark[i] = True
                    do_arr[i] = "R"
                    i += 1
        print(do_arr)
        print(mark)
        return "".join(do_arr)