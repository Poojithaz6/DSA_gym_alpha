class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        ans = []

        for num in nums:
            x = num if num > 0 else -num
            i = x - 1

            if nums[i] < 0:
                ans.append(x)
            else:
                nums[i] = -nums[i]

        return ans