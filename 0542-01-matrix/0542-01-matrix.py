class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols = len(mat),len(mat[0])
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = float('inf')
        
        while queue:
            row, col = queue.popleft()

            for dr,dc in dir:
                new_r,new_c = row+dr,col +dc
                if 0<=new_r<rows and 0<=new_c<cols and mat[new_r][new_c] > mat[row][col]:
                    mat[new_r][new_c] = mat[row][col]+1
                    queue.append((new_r,new_c))
        return mat
