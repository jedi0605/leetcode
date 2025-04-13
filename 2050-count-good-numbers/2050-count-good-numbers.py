class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 +7
        def help(base, power):
            if power == 0:
                return 1
            if power == 1:
                return base
            res = help(base, power//2)
            if power%2==1:
                return (res * base * res) % MOD
            return (res * res) % MOD
        even_num = ceil(n / 2)
        odd_num = n //2
        return (help(5,even_num) * help(4,odd_num)) % MOD
        # res = 0
        # for i in range(n):
        #     if i == 0:
        #         res = 5
            
        #     elif i % 2 == 0:
        #         res = (res*5 )%MOD
        #     else:
        #         res = (res*4)%MOD 
        # return res