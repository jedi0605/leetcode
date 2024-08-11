class Solution:
    # prefix sum
    def __init__(self, w: List[int]):
        # [1,3,2] => using prefix sum [1,4,6] => random pick nums => using bs seach to find the idx
        self.total = 0
        self.arr = []
        for wei in range(len(w)):
            self.total += w[wei]
            self.arr.append(self.total)

    def pickIndex(self) -> int:
        # self.total
        num = random.randint(1, self.total)
        l, r = -1, len(self.arr)
        while l + 1 != r:
            mid = (l + r) // 2
            if self.arr[mid] < num:
                l = mid
            else:
                r = mid
        return 0 if r == len(self.arr) else r
        # return bisect_left(self.arr, num)

    # # brute force
    # def __init__(self, w: List[int]):
    #     # [1,3] => [1,2,2,2] means index 1 have 1weight, index 2 have 3 weight
    #     self.arr = []
    #     for wei in range(len(w)):
    #         for _ in range(w[wei]):
    #             self.arr.append(wei)

    # def pickIndex(self) -> int:
    #     return random.choice(self.arr)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
