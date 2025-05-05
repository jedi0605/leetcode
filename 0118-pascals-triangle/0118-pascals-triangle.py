class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # res = []
        def dfs(rows):
            if rows == 1:
                return [[1]]

            tmp = dfs(rows - 1)
            pre_row = tmp[-1]
            new_row = [1]
            for i in range(1, len(pre_row)):
                new_row.append(pre_row[i - 1] + pre_row[i])
            print(new_row)
            new_row.append(1)
            tmp.append(new_row)
            return tmp

        res = dfs(numRows)
        return res
