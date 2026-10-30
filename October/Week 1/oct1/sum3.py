class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        used = set()

        for i in range(len(nums) - 2):
            seen = set()

            for j in range(i + 1, len(nums)):
                a = nums[i]
                b = nums[j]
                c = -a - b

                if c in seen:
                    x, y, z = a, b, c

                    if x > y:
                        x, y = y, x
                    if y > z:
                        y, z = z, y
                    if x > y:
                        x, y = y, x

                    key = (x, y, z)
                    if key not in used:
                        ans.append([x, y, z])
                        used.add(key)

                seen.add(b)

        return ans