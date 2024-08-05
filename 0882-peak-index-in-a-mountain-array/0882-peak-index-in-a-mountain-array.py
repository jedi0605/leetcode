class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = -1, len(arr)
        maxPeak = float("-inf")
        while l+1 != r:
            mid = (l+r) // 2
            if arr[mid-1] <arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            # go up or go down
            go_up = False
            if arr[mid]< arr[mid+1]:
                go_up = True
            
            if go_up == False:
                r = mid
            else:
                l = mid

        return l 

        # for i in range(len(arr)):
        #     if arr[i] > arr[i+1]:
        #         return i