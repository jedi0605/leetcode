class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        print(hours)

        idx =  bisect.bisect_left(hours, target)
        return len(hours) -idx