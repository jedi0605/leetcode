class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        right_map = {c:idx for idx,c in enumerate(s)}
        print(right_map)
        stack = []
        seen = set()

        for idx,c in enumerate(s):
            if c not in seen:
                while stack and c<stack[-1] and idx < right_map[stack[-1]]:
                    pop_c =  stack.pop()
                    seen.remove(pop_c)
                stack.append(c)
                seen.add(c)
        return ''.join(stack)