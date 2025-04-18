class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_cnt = Counter(p)
        print(p_cnt)
        s_sub = Counter()
        res = []
        l = 0
        for i in range(len(s)):
            if (i- l + 1) < len(p): # init
                s_sub[s[i]]+=1
            else:
                s_sub[s[i]]+=1
                if s_sub == p_cnt:
                    res.append(l)
                
                s_sub[s[l]]-=1
                if s_sub[s[l]] == 0:
                    s_sub.pop(s[l])
                l+=1
        return res
