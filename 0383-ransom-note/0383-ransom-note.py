class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = Counter(magazine)
        for c in ransomNote:
            if c not in cnt:
                return False
            if cnt[c] == 0:
                return False
            else:
                cnt[c]-=1
        return True