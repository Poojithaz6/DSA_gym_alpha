class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)

        def search(x):
            l = 0
            r = n

            while l < r:
                m = (l + r) // 2
                if arr[m] < x:
                    l = m + 1
                else:
                    r = m

            return l

        for i in (n // 4, n // 2, 3 * n // 4):
            x = arr[i]
            j = search(x)

            if j + n // 4 < n and arr[j + n // 4] == x:
                return x

        return arr[0]