#BF: search all until prev is greater that next
class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        for i in range(len(arr)+1):
            if arr[i]>arr[i+1]:
                return i
#optimal: o(logn): search space reduce