class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,r = -1, len(letters)

        while l+1 != r:
            mid = (l+r)//2
            c = letters[mid]

            if c <= target:
                l = mid
            else:
                r = mid

        return letters[r] if r != len(letters) else letters[0]