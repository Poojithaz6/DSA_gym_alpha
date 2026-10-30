class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        n = len(arr)

        for i in range(0, n, 2 * k):
            l = i
            r = min(i + k - 1, n - 1)

            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        ans = ""

        for ch in arr:
            ans += ch

        return ans