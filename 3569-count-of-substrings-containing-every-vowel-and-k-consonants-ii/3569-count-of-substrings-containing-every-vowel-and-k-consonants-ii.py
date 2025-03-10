class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleast(k):
            cnt = defaultdict(int)
            non_vowel = 0
            l = 0
            res = 0
            for r in range(len(word)):
                if word[r] in "aeiou":
                    cnt[word[r]] += 1
                else:
                    non_vowel += 1
                while len(cnt) == 5 and non_vowel >= k:
                    res += len(word) - r
                    if word[l] in "aeiou":
                        cnt[word[l]] -= 1
                    else:
                        non_vowel -= 1
                    if cnt[word[l]] == 0:
                        cnt.pop(word[l])
                    l += 1
            return res

        return atleast(k) - atleast(k + 1)
