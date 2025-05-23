class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # k is window Size        
        vow_cnt = 0
        max_cnt = 0
        for i in range(k):
            if s[i] in "aeiou":
                vow_cnt += 1
        max_cnt = vow_cnt
        for i in range(k,len(s)):
            # remove i-k
            if s[i] in "aeiou":
                vow_cnt += 1
            if s[i-k] in "aeiou":
                vow_cnt -= 1            
            max_cnt = max(vow_cnt, max_cnt)
        return max_cnt
