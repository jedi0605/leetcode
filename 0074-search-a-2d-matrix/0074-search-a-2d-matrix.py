class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bSearch(arr,target):
            l,r = -1,len(arr)
            while l+1!=r:
                mid = (l+r)//2
                if arr[mid] < target:
                    l = mid
                else:
                    r = mid
            
            if r == len(arr):
                return False
            else:
                return True if arr[r] == target else False
        # target row
        for row in matrix:
            if row[0] <= target <=row[-1]:
                # check this row
                print(row)
                return bSearch(row,target)
        return False