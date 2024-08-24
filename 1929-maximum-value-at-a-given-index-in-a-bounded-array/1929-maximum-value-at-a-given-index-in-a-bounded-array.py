class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def worked(max_num):

            # 1 2 3 4.  3 2 1
            # .    l mid r
            m = max_num - 1  # avoid th middle part
            l = index
            r = n - index - 1
            lsum, rsum = 0, 0
            if l > m:
                lsum = m * (m + 1) // 2 + l - m
            else:
                lsum = m * (m + 1) // 2 - (m - l) * (m - l + 1) // 2
            if r > m:
                rsum = m * (m + 1) // 2 + r - m
            else:
                rsum = m * (m + 1) // 2 - (m - r) * (m - r + 1) // 2
            return lsum+rsum+max_num <=maxSum
            # right

        # def worked(max_num):
        #     l,r = index -1 ,index +1
        #     arr = [1] * n
        #     arr[index] = max_num
        #     while l >=0 or r<=n-1:
        #         max_num -=1
        #         if l >=0:
        #             arr[l] = max_num if max_num>=1 else 1
        #             l -=1
        #         if r <=n -1:
        #             arr[r] = max_num if max_num>=1 else 1
        #             r+=1
        #     # print(arr)
        #     return sum(arr) <= maxSum
        l, r = 0, maxSum
        res = 0
        while l <= r:
            m = (l + r) // 2
            if worked(m):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res
