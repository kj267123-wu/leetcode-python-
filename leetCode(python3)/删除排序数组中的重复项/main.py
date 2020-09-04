import math
import numpy as np
from gettext import find
from typing import List
from numpy.core.fromnumeric import sort
from nt import remove

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums))[::-1]:
            if i-1 != -1:
                if nums[i-1] == nums[i]:
                    del nums[i] 
        return len(nums),nums

if __name__ == '__main__':
    n = [1,1,2]
    sol = Solution()
    length,result = sol.removeDuplicates(n)
    a = 1
