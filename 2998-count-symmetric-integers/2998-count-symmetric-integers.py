class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSym(num):
            num_s = str(num)
            if len(num_s) % 2 == 1:
                return False
            nx = len(num_s) // 2
            first = num_s[:nx]
            last = num_s[nx:]
            f_sum = 0
            l_sum = 0
            for i in range(len(first)):
                f_sum += int(first[i])
                l_sum += int(last[i])
            print(f"{first},{last} {f_sum},{l_sum}")

            return f_sum == l_sum

        res = 0
        for i in range(low, high + 1):
            if isSym(i) == True:
                res += 1
        return res
