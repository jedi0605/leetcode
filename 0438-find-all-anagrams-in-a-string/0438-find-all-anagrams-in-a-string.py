class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        win_count = Counter(p)
        sub_str = s[:window]
        s_count = Counter(sub_str)
        print(win_count)
        print(s_count)
        res = []
        for i in range(window, len(s)):
            if s_count == win_count:
                res.append(i - window)
            # remove i - 1
            s_count[s[i - window]] -= 1
            s_count[s[i]] += 1
        if s_count == win_count:
            res.append(len(s)-window)
        return res
