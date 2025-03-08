class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_op = math.inf
        start = blocks[:k]
        cnt = Counter(start)
        res = math.inf
        s = 0
        e = k - 1
        while e+1 < len(blocks):
            res = 0 if cnt["B"] >= k else min(res, k - cnt["B"])

            s_cht = blocks[s]
            cnt[s_cht] -= 1
            s += 1
            e += 1
            e_cht = blocks[e]
            cnt[e_cht] += 1
        res = 0 if cnt["B"] >= k else min(res, k - cnt["B"])

        return res
