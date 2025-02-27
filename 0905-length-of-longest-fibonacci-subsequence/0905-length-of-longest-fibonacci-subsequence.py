class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res = 0
        arr_set = set(arr)
        for i in range(len(arr) - 1):
            sub_len = 0
            for j in range(i + 1, len(arr)):
                a, b = arr[i], arr[j]
                cnt = 0
                while a + b in arr_set:
                    target = a + b
                    a = b
                    b = target
                    cnt += 1
                sub_len = 0 if cnt == 0 else 2 + cnt
                res = max(res, sub_len)
        return res
