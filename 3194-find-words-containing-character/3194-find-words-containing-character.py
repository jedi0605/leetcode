class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []

        for idx, s in enumerate(words):
            if x in s:
                res.append(idx)
        return res
