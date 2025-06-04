class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # from left?
        print(cardPoints[:k])
        left_sum = sum(cardPoints[:k])
        right_sum = 0
        max_sum = left_sum
        for i in range(k):
            left_sum -= cardPoints[k-i-1]
            right_sum += cardPoints[len(cardPoints)-i-1]
            total = left_sum+right_sum
            max_sum = max(max_sum,total)
        return max_sum