class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        extend_c = colors + colors[: k - 1]
        dp = [1] * len(extend_c)
        for i in range(1, len(dp)):
            if extend_c[i - 1] != extend_c[i]:
                dp[i] += dp[i - 1]
        print(dp)
        res = 0
        for n in dp:
            if n>=k:
                res+=1
        return res
        # print(extend_c)
        # res = 0
        # # [0,1,0,1,0]
        # # pre = 0
        # # j = 3
        # # res =1
        # for i in range(0, len(colors)):
        #     pre = extend_c[i]
        #     j = i + 1
        #     while j < i + k:
        #         cur = extend_c[j]
        #         if pre == cur:
        #             break
        #         pre = cur
        #         j += 1
        #     if j == k+i:
        #         res += 1
        # return res
