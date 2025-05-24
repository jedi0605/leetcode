class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        sub_sum = sum(arr[:k])
        if sub_sum / k >= threshold:
            res+=1
        
        for i in range(k,len(arr)):
            sub_sum=sub_sum - arr[i-k] + arr[i]
            if sub_sum / k >= threshold:
                res+=1
        return res



