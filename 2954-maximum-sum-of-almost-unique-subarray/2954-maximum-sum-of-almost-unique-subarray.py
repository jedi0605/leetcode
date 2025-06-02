class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        fit_request = []
        tmp = deque()
        max_res = 0

        for i in range(len(nums)):
            if len(tmp)<k:
                tmp.append(nums[i])
            elif len(tmp) == k:
                check_distinct = True if len(set(tmp)) >= m else False
                if check_distinct:
                    # fit_request.append(tmp.copy())
                    max_res = max(max_res, sum(tmp))
                tmp.popleft()
                tmp.append(nums[i])
        
        check_distinct = True if len(set(tmp)) >= m else False
        if check_distinct:
            max_res = max(max_res, sum(tmp))
        return max_res
        