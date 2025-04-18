class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_cnt = Counter(p)
        print(p_cnt)
        s_sub = Counter(s[:3])
        res = []
        for i in range(len(s) - len(p)+1):
            s_sub = Counter(s[i : (i + len(p))])
            if s_sub == p_cnt:
                res.append(i)
        return res
