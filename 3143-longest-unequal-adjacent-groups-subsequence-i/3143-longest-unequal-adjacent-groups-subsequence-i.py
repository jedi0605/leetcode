class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # find longest
        pre = groups[0]
        res = [words[0]]
        l = 0
        for i in range(1,len(groups)):
            if groups[i] != pre:
                res.append(words[i])
                pre = groups[i]
        return res

