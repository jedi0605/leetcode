class Solution:
    def getPrimeScores(self, nums: List[int]):
        prime_scores = []
        for n in nums:
            score = 0
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    score += 1
                    while n % f == 0:
                        n = n // f
            if n >= 2:
                score += 1
            prime_scores.append(score)
        return prime_scores
    
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        MOD = 10**9 + 7
        res = 1
        prime_scores = self.getPrimeScores(nums)
        
        left_bound = [-1] * N
        right_bound = [N] * N
        
        stack = []
        for i,s in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]] < s:
                index = stack.pop()
                right_bound[index] = i
            if stack:
                left_bound[i] = stack[-1]
            stack.append(i)
        print(left_bound)
        print(right_bound)

        min_heap = [ (-n,i) for i,n in enumerate(nums) ]
        heapify(min_heap)

        while k>0:
            n, index = heappop(min_heap)
            n = -n
            scoure = prime_scores[index]
            
            left_cnt = index - left_bound[index]
            right_cnt = right_bound[index] - index

            cnt = left_cnt * right_cnt
            op_times = min(k,cnt)
            res = (res *  pow(n,op_times,MOD)  ) %MOD
            k-= op_times
        return res
