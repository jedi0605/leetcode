class Solution:
    def maxVowels(self, s: str, k: int) -> int:        
        s_arr = list(s)
        res = 0
        vow_cnt = 0
        for i in range(k):
            if s_arr[i] in "aeiou":
                vow_cnt +=1
        res = max(vow_cnt,res)

        for i in range(k,len(s_arr)):
            pop_cht = s_arr[i-k]

            if pop_cht in "aeiou":
                vow_cnt-=1
            if s_arr[i] in "aeiou":
                vow_cnt+=1
            res = max(vow_cnt,res)
        return res