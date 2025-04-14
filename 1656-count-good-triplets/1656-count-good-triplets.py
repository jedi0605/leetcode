class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        possible = []
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    possible.append([i, j, k])
        res = 0
        for p1, p2, p3 in possible:
            if (
                abs(arr[p1] - arr[p2]) <= a
                and abs(arr[p2] - arr[p3]) <= b
                and abs(arr[p1] - arr[p3]) <= c
            ):
                res += 1
        return res
