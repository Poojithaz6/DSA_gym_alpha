class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for x in nums:
            i = abs(x) - 1
            if nums[i] > 0:
                nums[i] = -nums[i]

        ans = []
        for i in range(n):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans