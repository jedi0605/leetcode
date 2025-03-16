class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, min(ranks) * cars * cars

        def canRepairCar(mins):
            totalCar = 0
            for r in ranks:
                totalCar +=  int((mins / r) ** 0.5)
            if totalCar >= cars:
                return True
            return False

        while l <= r:
            mid = (l + r) // 2
            if canRepairCar(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
