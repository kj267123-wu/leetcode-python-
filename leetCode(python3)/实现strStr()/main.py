class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1

L1 = 'hello'
L2 = 'll'
sol = Solution()
result = sol.strStr(L1,L2)
a = 1