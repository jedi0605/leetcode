class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        sub_set = defaultdict(int)
        for i in range(k):
            sub_set[s[i]]+=1
        print(sub_set)
        res = 0
        if len(sub_set) == k :
            res+=1
        for i in range(k,len(s)):
            pre_cht =s[i-k]
            sub_set[pre_cht]-=1
            if sub_set[pre_cht] == 0:
                del sub_set[pre_cht]
            sub_set[s[i]]+=1
            if len(sub_set) == k :
                res+=1
        return res
