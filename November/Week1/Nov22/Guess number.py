#BF: chech all numbers O(n)
class Solution:
    def guessNumber(self, n: int) -> int:
        for i in range(n+1):
            if guess(i)==0:
                return i