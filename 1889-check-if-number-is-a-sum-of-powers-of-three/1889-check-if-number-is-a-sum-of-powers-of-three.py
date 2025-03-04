class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        p_set = set()
        arr = []
        for i in range(15):
            p_set.add(3**i)
            arr.append(3**i)
        i = len(arr) -1
        while i >0:
            if n >= arr[i]:
                break
            i -= 1
        while i >= 0:
            if n >= arr[i]:
                n = n-arr[i]
            if n == 0:
                return True
            i-=1
        return n == 0            


        


        