class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # k is window Size
        cnt = deque()
        vow_cnt = 0
        max_cnt = 0
        for i in range(len(s)):
            if len(cnt) < k:
                cnt.append(s[i])
                if s[i] in "aeiou":
                    vow_cnt += 1
            else:
                pop_s = cnt.popleft()
                if pop_s in "aeiou":
                    vow_cnt -= 1
                cnt.append(s[i])
                if s[i] in "aeiou":
                    vow_cnt += 1
            max_cnt = max(vow_cnt, max_cnt)
        return max_cnt
