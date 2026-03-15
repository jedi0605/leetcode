class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        # tmp = 0
        # # 1_004_590
        # for i in range(n+1):
        #     if i > 999 and i < 1_000_000:
        #        tmp +=1
        #     if i > 1_000_000 -1 and i < 1_000_000_000:
        #         tmp+=2
        #     if i > 1_000_000_000 -1 and i < 1_000_000_000_000:
        #         tmp+=3
        #     if i > 1_000_000_000_000 -1 and i < 1_000_000_000_000_000:
        #         tmp+=4
        #     if i > 1_000_000_000_000_000 -1 and i < 1_000_000_000_000_000_000:
        #         tmp+=5
        # print(f"test: {tmp}")

        # return tmp  
        # total = 0
        # if n > 1_000_000:
        #     total += 1_000_000 - 1000
        # else:
        #     total += n - 1000 + 1
        #     return total
        total = 0
        if n > 1000 - 1:
            total += n - 1000 + 1
        if n > 1_000_000 - 1:
            total += n - 1_000_000 + 1
        if n > 1_000_000_000 - 1:
            total += n - 1_000_000_000 + 1
        if n > 1_000_000_000_000 - 1:
            total += n - 1_000_000_000_000 + 1
        if n > 1_000_000_000_000_000 - 1:
            total += n - 1_000_000_000_000_000 + 1
            
        return total   
        # if n > 1_000_000_000:
        #     total += (1_000_000_000 - 1_000_000 - 1000) * 2
        # else:
        #     total += (n - 1_000_000+ 1) * 2
        #     return total

        # if n > 1_000_000_000_000:
        #     total+= (1_000_000_000_000 - 1_000_000_000 -1_000_000 - 1000) * 3
        # else:
        #     total += (n - 1_000_000_000 + 1) * 3
        #     return total

        # if n > 1_000_000_000_000_000:
        #     total+= (n - 1_000_000_000_000 + 1) * 4
        # else:
        #     total += (n - 1_000_000_000_000 + 1) * 4
        #     return total

        
        # if n > 1_000_000_000_000_000_000:
        #     total+= (n - 1_000_000_000_000_000 + 1) * 5
        # else:
        #     total += (n - 1_000_000_000_000_000 + 1) * 5
        #     return total
        # return total
        # # 1008182
            
