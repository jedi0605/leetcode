class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        win_count = Counter(p)
        res = []
        for i in range(0, len(s) - window + 1):
            sub_s = s[i : i + window]
            sub_counter = Counter(sub_s)
            if sub_counter == win_count:
                res.append(i)
        return res
