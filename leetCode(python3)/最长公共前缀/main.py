class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans

L1 = ["flower","flow","flight"]
sol = Solution()
result = sol.longestCommonPrefix(L1)
a = 1