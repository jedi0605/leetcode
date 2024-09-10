class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for arr in matrix:
            if arr[0]<= target <= arr[-1]:
                print(arr)
                idx= bisect_left(arr, target)
                return arr[idx] == target
        return False