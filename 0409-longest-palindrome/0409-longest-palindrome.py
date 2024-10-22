class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        print(cnt)
        odd = 0
        other = 0
        flag = 0
        for cht, val in cnt.items():
            print(f"{cht}, {val}")
            if val % 2 == 0:
                other += val
            else:
                odd += val // 2 * 2                
                flag = 1
        
        return other + odd + flag
        
