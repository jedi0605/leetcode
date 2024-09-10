class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def b_search2(start, end):
            l, r = start -1 , end
            while l + 1 != r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid
                else:
                    r = mid
            if r == end:
                return -1
            return r if nums[r] == target else -1

        ## find smallest index
        def b_search():
            l, r = 0, len(nums)
            while l + 1 != r:
                mid = (l + r) // 2
                if nums[mid] > nums[l]:
                    l = mid
                else:
                    r = mid
            return r

        print(b_search())
        idx = b_search()
        start, end = 0, 0

        if nums[0] <= target <= nums[idx - 1]:
            start, end = 0, idx
        else:
            start, end = idx, len(nums)
        print(f"{start},{end}")
        return b_search2(start, end)
