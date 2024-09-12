class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = -1, len(arr)

        while l+1 !=r :
            mid = (l+r) // 2
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid

            if arr[mid]> arr[mid+1]:
                r = mid
            else:
                l = mid
        return -1

        # brute force
        # for i in range(len(arr)-1):
        #     if arr[i] > arr[i+1]:
        #         return i