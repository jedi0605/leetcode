class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque()
        q.append(s)
        visited = set()
        while q:
            cur_str = q.pop()
            for w in wordDict:
                if cur_str.startswith(w) and cur_str not in visited:
                    tmp_str = cur_str[len(w):]
                    if tmp_str == "":
                        return True
                    q.append(cur_str[len(w):])
            visited.add(cur_str)
        return False

