class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = Counter(s)

        for ch in t:
            cnt[ch] -= 1
        count = 0
        for key,val in cnt.items():
            count += abs(val)
        return count //2
