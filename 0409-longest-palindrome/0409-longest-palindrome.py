class Solution:
    def longestPalindrome(self, s: str) -> int:
        print(1//2)
        cnt = Counter(s)

        print(cnt)
        big_odd_key = ""
        big_odd_val = 0
        for key, val in cnt.items():
            if val % 2 == 1:
                if big_odd_val < val:
                    big_odd_key = key
        res = 0
        if big_odd_key != "":
            res += cnt[big_odd_key]
            cnt[big_odd_key] = 0

        for key, val in cnt.items():
            if val % 2 == 0:
                res+=cnt[key]
                cnt[key] = 0
            else:
                res+= (cnt[key] // 2) * 2
        return res
                
        # find biggest odd as center
