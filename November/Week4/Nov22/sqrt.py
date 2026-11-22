#BF: check everyyyyyy number! O(n)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        sqrt=0
        for i in range(1,x):
            if i*i<=x:
                sqrt=i
        return sqrt
#Optimal: binary search reduce the search space::: short down the search space and keep looping
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        low = 1
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1

            else:
                low = mid + 1
                sqrt = mid
        return sqrt