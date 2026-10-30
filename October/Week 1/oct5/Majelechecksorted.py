class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        l = 0
        r = len(nums)

        while l < r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            else:
                r = m

        i = l + len(nums) // 2

        return i < len(nums) and nums[i] == target