class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        for i in range(len(digits)):
            
            for j in range(len(digits)):
                
                for k in range(len(digits)):
                    if i == j or j == k or k== i:
                        continue
                    tmp = digits[i]* 100 + digits[j]* 10 + digits[k]

                    if tmp >=100 and digits[k] % 2 == 0:
                        res.add(tmp)
        print(res)
        arr = sorted(list(res))
        return arr
