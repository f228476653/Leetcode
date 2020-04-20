
class Solution:
    def mySqrt1(self, x: int) -> int:
        if x<= 1 :return x
        i = 2
        while i<= x//2+1:
            if i * i > x: return i-1
            if i * i == x: return i
            i+=1
# Runtime: 6192 ms, faster than 5.01% of Python3 online submissions for Sqrt(x).
# Memory Usage: 13.9 MB, less than 6.45% of Python3 online submissions for Sqrt(x).


    def mySqrt2(self, x: int) -> int: #二分法
        if x < 2 :return x
        left, right = 1, x
        mid = 0
        while left <= right:
            mid = left + (right - left) // 2 #just 1 bigger than half
            if mid* mid == x: return mid
            if mid* mid > x: 
                right = mid-1
            else:
                left = mid+1
        return right

s = Solution()
m = s.mySqrt2(3)
print(m)