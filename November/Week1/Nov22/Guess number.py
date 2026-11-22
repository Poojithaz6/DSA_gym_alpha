#BF: chech all numbers O(n)
class Solution:
    def guessNumber(self, n: int) -> int:
        for i in range(n+1):
            if guess(i)==0:
                return i

#optimal: reduce the search space using guess results o(logn)
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        while low <= high:
            mid = (low + high) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) > 0:
                low = mid + 1
            else:
                high = mid - 1

