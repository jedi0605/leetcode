class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        current = defaultdict(int)
        res = 0
        l = 0
        # r=0 l =0
        # c={a}
        # r=1 l=0
        # c={a,b}
        # r=2 l=0
        # c={a,b,c}. res = 6-2 =4
        #   cur={b,c} l=1

        for r in range(len(s)):
            current[s[r]] += 1
            if len(current) == 3:

                while len(current) == 3 and l < len(s):
                    res += (len(s) - r)
                    current[s[l]] -= 1
                    if current[s[l]] == 0:
                        current.pop(s[l])
                    l += 1
        return res
