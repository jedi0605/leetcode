class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)

        init_arr = cardPoints[:k] # choose left k
        init_sum = sum(init_arr)
        max_sum = init_sum
        m =  len(cardPoints)
        for i in range(k):
            # end of the cur arr
            end_num = cardPoints[k - i -1]
            print(end_num)
            init_sum -= end_num

            # add right of the k
            right_num = cardPoints[m - i -1]
            print(right_num)
            init_sum += right_num
            max_sum = max(max_sum,init_sum)
        return max_sum
