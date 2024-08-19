class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def canSplit(mid):
            total = 0
            chunk = 0
            for s in sweetness:
                total += s
                if total >= mid:
                    total = 0
                    chunk += 1
            return chunk >= k + 1

        l, r = min(sweetness), sum(sweetness)
        ans = 1
        while l<= r:
            mid = (l + r) // 2
            if canSplit(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid -1
        return ans

        # def dfs(start, remaining_chunks, current_split):
        #     if remaining_chunks == 0:
        #         if start == n:
        #             result.append(current_split[:])
        #         return

        #     for i in range(start, n):
        #         chunk = sweetness[start:i+1]
        #         current_split.append(chunk)
        #         dfs(i + 1, remaining_chunks - 1, current_split)
        #         current_split.pop()

        # dfs(0, k+1, [])
        # global_max = float("-inf")
        # for r in result:
        #     local_min = float("inf")
        #     for sub_arr in r:
        #         local_min =min(local_min, sum(sub_arr))
        #     global_max = max(global_max,local_min)
        # return global_max
