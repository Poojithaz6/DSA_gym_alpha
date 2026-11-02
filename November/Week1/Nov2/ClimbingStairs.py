#Brute force
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)
#optimal
    def climbStairs2(self,n):
        if n<=2:
            return n
        a,b=1,2
        for i in range(3,n+1):
            a,b=b,a+b
        return b