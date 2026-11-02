#bf
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)

        def solve(pos, step, k):
            if step == 0:
                return pos == target

            return solve(pos+step, step-1, k) or solve(pos-step, step-1, k)

        k = 0

        while True:
            if solve(0, k, k):
                return k
            k += 1
#optimal
    def reachNumber(self, target: int) -> int:
        target = abs(target)

        total = 0
        steps = 0

        while total < target or (total - target) % 2 != 0:
            steps += 1
            total += steps

        return steps