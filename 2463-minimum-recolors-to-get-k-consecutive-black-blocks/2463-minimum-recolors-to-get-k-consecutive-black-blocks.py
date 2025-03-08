class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_op = math.inf
        if len(blocks) == k:
            cnt = Counter(blocks)            
            return 0 if cnt["B"]>=k else k - cnt["B"]
        for i in range(0, len(blocks) - k+1, 1):
            op = 0
            for j in range(i, i+k):
                if blocks[j] != "B":
                    op += 1
            min_op = min(op, min_op)
        return min_op
