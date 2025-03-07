class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right + 1)  # 0....right
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(sqrt(right)) + 1):
            if is_prime[i]:
                for j in range(i + i, right + 1, i):
                    is_prime[j] = False
        only_prime = []
        for i in range(left, right + 1, 1):
            if is_prime[i]:
                only_prime.append(i)
        if len(only_prime) < 2:
            return [-1, -1]
        
        diff = float("inf")
        res = []
        for i in range(1,len(only_prime),1):
            pre = only_prime[i-1]
            cur = only_prime[i]
            if cur - pre < diff:
                diff = cur - pre
                res = [pre,cur]
        return res
        # min_heap = []

        # for i in range(len(only_prime) - 1, -1, -1):
        #     curr = only_prime[i]
        #     if i - 1 < 0:
        #         break
        #     pre = only_prime[i - 1]
        #     diff = curr - pre
        #     heappush(min_heap, (diff, pre, curr))
        # diff, pre, cur = heappop(min_heap)
        # return [pre, cur]
