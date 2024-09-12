class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)
        print(idx)

        l, r = idx - 1, idx
        while k > 0:
            if l < 0:
                r += 1
            elif r == len(arr):
                l -= 1
            elif x - arr[l] <= arr[r] - x:
                l -= 1
            else:
                r += 1
            k -= 1
            print(f"{l},{r}")
        return arr[l + 1 : r]
        # dis_idx = []
        # for i in range(len(arr)):
        #     dis_idx.append([abs(arr[i] - x), i])
        # print(dis_idx)
        # dis_idx = sorted(dis_idx, key=lambda x: (x[0], x[1]))
        # print(dis_idx)
        # res = []
        # for i in range(k):
        #     res.append(arr[dis_idx[i][1]])

        # return sorted(res)
