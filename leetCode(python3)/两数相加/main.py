from __future__ import absolute_import
import addTwoNumbers

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

#class Solution:
 #   def addTwoNumbers(self, L1:ListNode, L2:ListNode) -> ListNode:
  #      return ListNode(None)

if __name__ == '__main__':
    array1 = [2,4,3]
    array2 = [5,6,4]
    L1 = ListNode(None)
    v1 = ListNode(None)
    for i,val in enumerate(array1):
        if i == 0:
            L1 = ListNode(val)
            v1 = L1
        else:
            L1.next = ListNode(val)
            v1 = L1.next
    L2 = ListNode(None)
    v2 = ListNode(None)
    for i,val in enumerate(array2):
        if i == 0:
            L2 = ListNode(val)
            v1 = L2
        else:
            L2.next = ListNode(val)
            v2 = L2.next
    sol = Solution()
    result = sol.addTwoNumbers(L1,L2)

