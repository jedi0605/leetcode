class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        # for i in range(len(arr)):
        #     for j in range(i, len(arr)):
        #         if sum(arr[i : j + 1]) % 2 == 1:
        #             res += 1
        cur_sum = 0
        odd_cnt = 0
        event_cnt = 0
        MOD = 10**9 + 7
        for a in arr:
            cur_sum += a
            if cur_sum % 2 == 1:
                res = (1 + event_cnt + res) % MOD

                odd_cnt += 1
            else:
                res = (odd_cnt + res) % MOD
                event_cnt += 1
        return res
