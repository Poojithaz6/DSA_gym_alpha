class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        w = valueDiff + 1
        d = {}

        for i in range(len(nums)):
            x = nums[i]
            b = x // w

            if b in d:
                return True
            if b - 1 in d and x - d[b - 1] <= valueDiff:
                return True
            if b + 1 in d and d[b + 1] - x <= valueDiff:
                return True

            d[b] = x

            if i >= indexDiff:
                old = nums[i - indexDiff] // w
                del d[old]

        return False