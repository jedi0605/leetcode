class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def normalize(N):
            ans = 0
            less = False  # whether the converted number is less than N
            for n in range(len(str(N))):
                digi = int(str(N)[n])
                if less:
                    ans = ans * 10 + limit
                elif digi > limit:
                    less = True
                    ans = ans * 10 + limit
                else:
                    ans = ans * 10 + digi
            return ans           

        def count(N):
            ans = 0
            base = limit + 1
            prefix = str(N)[: -len(s)]
            for n in prefix:
                ans = ans * base + int(n)
            if int(prefix + s) <= N:
                ans += 1
            return ans

        print(normalize(1200))
        return count(normalize(finish)) - count(normalize(start - 1))
