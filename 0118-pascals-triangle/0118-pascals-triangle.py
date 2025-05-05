class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            cur_row = [1] * (i+1)
            print(cur_row)
            for j in range(1,i):
                cur_row[j] = res[-1][j-1]+ res[-1][j]

            res.append(cur_row)
        return res