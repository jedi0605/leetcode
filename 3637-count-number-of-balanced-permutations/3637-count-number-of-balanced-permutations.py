class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        arr = []
        for e in num:
            arr.append(int(e))
        hs = Counter(arr)

        print(hs)

        @cache
        def dfs(node, q, t, sm):

            if node == 10:
                # print("-")
                if t == 0 and q ==0:
                    if sm == 0:
                        return 1
                return 0
            # print(node,sm, sm1)
            ans = 0
            # for node in range(nd, 10):
            # print(sm, node, q, t)
            tmp = hs[node]
            for j in range(tmp + 1):
                if j > q or t < tmp - j: continue
                
                ways = comb(q, j) * comb(t, (tmp - j))

                diff = sm + ((j * node) - ((tmp - j) * node))

                ans += (ways * dfs(node + 1, q - j, t - (tmp - j), diff))
                
            # if t >= i and q >= (tmp - i):
            #     ans += dfs(node + 1, q - i, sm + (i * node) - ((tmp - i) * node))
            
            return ans % (10 ** 9 + 7)
        
        return (dfs(0, n // 2, n - (n // 2), 0))
        # # using backtraking to list all permutations
        # res_set = set()
        # tmp = []
        # digi_nums = [int(num[i]) for i in range(len(num))]  # num to digit
        # # print(digi_nums)
        # visited = set()  # record index

        # def backtraking():
        #     # print(tmp)
        #     if len(tmp) == len(digi_nums):

        #         res_set.add(tuple(tmp.copy()))
        #         return
        #     for i in range(len(digi_nums)):
        #         if i not in visited:
        #             visited.add(i)
        #             tmp.append(digi_nums[i])
        #             backtraking()
        #             tmp.pop()
        #             visited.remove(i)

        # backtraking()
        # res = 0
        # for arr in res_set:
        #     even_c, odd_c = 0, 0
        #     for i in range(len(arr)):
        #         if i % 2:
        #             even_c += arr[i]
        #         else:
        #             odd_c += arr[i]
        #     if even_c == odd_c:
        #         res += 1
        # return res
