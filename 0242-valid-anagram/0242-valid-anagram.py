class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        cnt = Counter(s)
        print(cnt)
        for cht in t:
            if cht not in cnt or cnt[cht] == 0:
                return False
            cnt[cht] -=1
            
        return sum(cnt.values()) == 0