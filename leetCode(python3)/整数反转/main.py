class Solution:
    def reverse(self, x: int) -> int:

        rev = 0
        intmax = 2147483647  # python3 最大整数sys.maxsize为2^63
        intmin = -2147483648

        while x!=0:
            if x>0:
                num = x%10 # 3
                x = x//10  #12
            else:
                num = x%-10
                x = -(x//-10)
            print(num)
            print(x)

            # ((0*10+3)*10+2)*10+1
            # 在这个阶段可能小的数变大了，所以需要判断是不是会导致整数溢出
            if rev>intmax//10 or (rev==intmax//10 and num > 7): return 0
            if rev<-(intmin//-10) or (rev==-(intmin//-10) and num <-8): return 0
            temp = rev * 10 + num
            rev = temp
            # 不能对最后乘过10后的最终结果进行判断是否溢出，因为如果溢出，计算出来的结果都是错误的，还怎么和最大值比较，所以在乘10的上一步就进行比较
        return rev

l1 = 123
sol = Solution()
result = sol.reverse(l1)
a = 1