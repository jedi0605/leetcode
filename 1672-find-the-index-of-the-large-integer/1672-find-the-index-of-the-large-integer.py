# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
# 	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
# 	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
# 	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
# 	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
# 	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: "ArrayReader") -> int:
        arr_len = reader.length()
        print(arr_len)
        l, r = 0, arr_len - 1

        while l < r:
            mid = (l + r) // 2
            if mid - l > r - (mid + 1):
                l += 1  # make sure left arr, right arr are equal
            comp = reader.compareSub(l, mid, mid + 1, r)
            if comp == 0:
                return l - 1

            if comp == 1:
                r = mid
            elif comp == -1:
                l = mid + 1

        return l
