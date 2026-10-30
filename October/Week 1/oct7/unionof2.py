class Solution:
    def union(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq = {}

        for x in nums1:
            freq[x] = freq.get(x, 0) + 1

        for x in nums2:
            if x not in freq or freq[x] == 0:
                freq[x] = 1
            else:
                freq[x] += 1

        ans = []

        for x in freq:
            ans.append(x)

        return ans