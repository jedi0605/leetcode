class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        total, res, even_c, odd_c = 0,0,0,0
        MOD = 10 ** 9 + 7
        for a in arr:
            total +=a
            if total %2 == 1: # odd
                odd_c+=1
                res = (res + 1 + even_c) % MOD
            else:
                even_c +=1
                res = (res + odd_c) % MOD
        
        return res