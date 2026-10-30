class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0

        for bit in range(32):
            count = 0
            mask = 1 << bit

            for num in nums:
                if num & mask:
                    count += 1

            if count % 3:
                ans |= mask

        if ans >= (1 << 31):
            ans -= (1 << 32)

        return ans