class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        position = {}  # n->(r,c)
        ROW = len(mat)
        COL = len(mat[0])
        for r in range(ROW):
            for c in range(COL):
                position[mat[r][c]] = (r, c)

        row_cnt = [0] * ROW
        col_cnt = [0] * COL
        for i in range(len(arr)):
            num = arr[i]
            n_r,n_c =  position[num]
            row_cnt[n_r]+=1
            col_cnt[n_c]+=1
            if row_cnt[n_r] == COL or col_cnt[n_c] == ROW:
                return i
