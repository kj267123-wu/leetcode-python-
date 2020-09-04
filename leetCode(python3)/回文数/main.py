class Solution:
    def isPalindrome(self, x: int) -> bool:
        #负数都不是回文数
        if x<0:
            return False
        #转换为字符串序列，便于处理
        x = str(x) 
        #进行对称的比较。偶数一一对照，奇数最中间的数不用比较
        for i in range(0,len(x)//2):
            # print(x[i],x[len(x) -1 -i]) #个人调试用
            if x[i] !=  x[len(x) -1 -i]:
                return False
        return True

L1 = 121
sol = Solution()
result = sol.isPalindrome(L1)
a = 1