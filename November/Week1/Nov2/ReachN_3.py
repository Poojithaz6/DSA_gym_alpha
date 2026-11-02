#BF
class Solution:
    def countWays(self, n):
        def solve(n):
            if n == 0:
                return 1

            if n < 0:
                return 0

            return solve(n-1) + solve(n-2) + solve(n-3)

        return solve(n)
#optimal
    def countWays2(self, n):
        if n == 0:
            return 1

        if n == 1:
            return 1

        if n == 2:
            return 2

        a, b, c = 1, 1, 2

        for i in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c