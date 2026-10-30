class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq = {}

        for x in nums1:
            freq[x] = freq.get(x, 0) + 1

        ans = []

        for x in nums2:
            if freq.get(x, 0) > 0:
                ans.append(x)
                freq[x] -= 1

        return ans