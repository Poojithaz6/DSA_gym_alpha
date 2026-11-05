#BF
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            x=1/x
            n=-n
            if n%2==0:
                return self.myPow(x,n//2)*self.myPow(x,n//2)

            else:
                return self.myPow(x,n//2)*self.myPow(x,n//2)*x
        if n>0:
            if n%2==0:
                return self.myPow(x,n//2)*self.myPow(x,n//2)

            else:
                return self.myPow(x,n//2)*self.myPow(x,n//2)*x
#More accurate recursion
    def myPow2(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)  # finding the reciprocal value after power calc in pos
        halfOfPow = self.myPow(x, n // 2)
        if n % 2 == 0:
            return halfOfPow * halfOfPow
        else:
            return halfOfPow * halfOfPow * x
