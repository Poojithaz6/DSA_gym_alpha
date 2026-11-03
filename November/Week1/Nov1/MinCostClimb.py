class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)

        def solve(i):
            if i >= n:
                return 0

            return cost[i] + min(solve(i+1), solve(i+2))

        return min(solve(0), solve(1))
#optimal
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a, b = 0, 0
        for i in range(len(cost) - 1, -1, -1):
            a, b = cost[i] + min(a, b), a

        return min(a, b)