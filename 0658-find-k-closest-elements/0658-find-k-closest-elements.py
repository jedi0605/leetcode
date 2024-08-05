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
