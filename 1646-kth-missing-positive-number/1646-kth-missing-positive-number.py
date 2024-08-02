class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        mapping = set(arr)
        cnt = 0
        res = 0
        for i in range(1,10000):
            if i not in mapping:
                cnt+=1
            if cnt == k:
                res= i
                break
        return res
            
  