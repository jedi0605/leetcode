class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def work2(max_val):
            mid = max_val -1
            r = n - index - 1 
            r_sum = 0
            l = index
            l_sum = 0
            if r > mid:
                r_sum = mid*(mid+1) // 2 + r-mid
            else:
                r_sum = mid*(mid+1)//2 - (mid-r) *(mid-r+1)//2
            if l>mid:   
                l_sum = mid*(mid+1) // 2 + l-mid
            else:
                l_sum = mid*(mid+1)//2 - (mid-l) *(mid-l+1)//2
            total = max_val+r_sum+l_sum
            return total <= maxSum
        # def work(max_val):
        #     if n == 0:
        #         return max_val <= maxSum

        #     next_val = max_val
        #     guess_arr = [1] * n
        #     guess_arr[index] = next_val

        #     l, r = index,index
        #     while l > 0 or r < n - 1:
        #         next_val = next_val - 1 if next_val > 1 else 1
        #         if l > 0:
        #             l -= 1
        #             guess_arr[l] = next_val
        #         if r != n - 1:
        #             r += 1
        #             guess_arr[r] = next_val
                    
        #     print(guess_arr)
        #     return sum(guess_arr) <= maxSum

        l,r = 1,maxSum
        ans = 0
        while l<=r:
            mid = (l+r) // 2
            if work2(mid):
                ans = mid
                l = mid+1
            else:
                r =mid-1
        
        return ans
