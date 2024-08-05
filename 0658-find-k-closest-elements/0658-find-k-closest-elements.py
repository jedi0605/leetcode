class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        left = bisect_left(arr, x) - 1
        right = left + 1

        print(f"left:{left} right:{right}")

        while k > 0:
            ### out of bound
            if left < 0:
                right += 1
            elif right == len(arr):
                left -= 1
            elif x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
            ### in bound
            k -= 1
        print(f"left:{left} right:{right}")

        return arr[left + 1 : right]


        # dis_idx = []

        # for i in range(len(arr)):
        #     dis_idx.append( (abs(arr[i] - x),i ))

        # print(dis_idx)
        # sorted_data = sorted(dis_idx, key=lambda x: (x[0], x[1]))
        # print(sorted_data)
        # res = []
        # for i in range(k):
        #     res.append(arr[  sorted_data[i][1]])
        # res.sort()
        # return res