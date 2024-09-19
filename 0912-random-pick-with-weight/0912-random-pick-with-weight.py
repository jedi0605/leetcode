class Solution:

    def __init__(self, w: List[int]):
        self.w_arr = []
        self.sum = 0
        for idx,weight in enumerate(w):
            self.sum+=weight
            self.w_arr.append(self.sum)
        print(self.w_arr)  
    def pickIndex(self) -> int:
        num =  random.randint(1, self.sum)
        return bisect.bisect_left(self.w_arr, num)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()