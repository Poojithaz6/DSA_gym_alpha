class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        x = 0

        for num in nums:
            x ^= num

        bit = x & -x
        a = 0
        b = 0

        for num in nums:
            if num & bit:
                a ^= num
            else:
                b ^= num

        return [a, b]