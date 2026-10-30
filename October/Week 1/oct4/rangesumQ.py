class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [0]
        total = 0

        for num in nums:
            total += num
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]