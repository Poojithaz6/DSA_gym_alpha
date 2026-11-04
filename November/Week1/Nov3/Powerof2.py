#BF recursive
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 2 or n == 1:  # 1 is always power of 2 and if n==2, then n/2 is 1 which will make it not divisible, thus have to set a default case
            return True
        if n == 0:
            return False

        if n % 2 == 0:
            return self.isPowerOfTwo(n / 2)
        else:
            return False
#optimal code o(n), bit manipulate
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0