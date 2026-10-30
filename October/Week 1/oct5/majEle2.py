class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        a = None
        b = None
        ca = 0
        cb = 0

        for num in nums:
            if num == a:
                ca += 1
            elif num == b:
                cb += 1
            elif ca == 0:
                a = num
                ca = 1
            elif cb == 0:
                b = num
                cb = 1
            else:
                ca -= 1
                cb -= 1

        ca = 0
        cb = 0

        for num in nums:
            if num == a:
                ca += 1
            elif num == b:
                cb += 1

        ans = []
        if ca > len(nums) // 3:
            ans.append(a)
        if cb > len(nums) // 3:
            ans.append(b)

        return ans