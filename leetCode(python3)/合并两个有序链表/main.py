class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

array1 = [1,2,4]
array2 = [1,3,4]
L1 = ListNode(None)
L2 = ListNode(None)
for i,val in enumerate(array1):
    if i == 0:
        L1 = ListNode(val)
        v1 = L1
    else:
        v1.next = ListNode(val)
        v1 = v1.next
for i,val in enumerate(array2):
    if i == 0:
        L2 = ListNode(val)
        v2 = L2
    else:
        v2.next = ListNode(val)
        v2 = v2.next

sol = Solution()
result = sol.mergeTwoLists(L1,L2)
a = 1

