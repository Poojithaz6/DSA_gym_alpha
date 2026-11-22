#BF: O(n)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<=1:
            return True
        for i in range(1,num):
            if i*i==num:
                return True
        return False
#optimal: O(logn)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<=1:
            return True
        low=1
        high=num
        sqrt =0
        while low<=high:
            mid=(low+high)//2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                low=mid+1
            else:
                high=mid-1
        return False