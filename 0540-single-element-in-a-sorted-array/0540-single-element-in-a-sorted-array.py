class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0, len(nums)

        while l<r:
            mid = (l+r) // 2

            if mid+1 <len(nums) and nums[mid] == nums[mid+1]:
                # choose right or left
                chooseRight = (len(nums) - mid -1)%2
                if chooseRight:
                    r = mid-1
                else:
                    l = mid+2
            elif mid -1 >=0 and nums[mid] == nums[mid-1]:
                chooseRight = (len(nums) - mid -1)%2
                if chooseRight == 0:
                    r = mid-2
                else:
                    l = mid  +1
            else:
                return nums[mid]
        return nums[l]

