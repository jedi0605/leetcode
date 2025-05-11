class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        start_odds = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                start_odds = 0
            else:
                start_odds += 1
                if start_odds == 3:
                    return True
        return False
