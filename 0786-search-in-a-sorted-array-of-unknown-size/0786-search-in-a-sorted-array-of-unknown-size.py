# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        l,r = -1 , 10_000
        while l + 1 !=r:
            mid = (l+r)//2
            print(mid)
            res = reader.get(mid)            
            if res == 2**31 -1:
                r = mid
                continue            
            if res < target:
                l = mid
            else:
                r = mid
        return r if reader.get(r) == target else -1 