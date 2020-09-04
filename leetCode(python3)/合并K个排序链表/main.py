from typing import List
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

array1 = [1,4,5]
array2 = [1,3,4]
array3 = [2,6]
L1 = ListNode(None)
L2 = ListNode(None)
L3 = ListNode(None)
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
for i,val in enumerate(array3):
    if i == 0:
        L3 = ListNode(val)
        v3 = L3
    else:
        v3.next = ListNode(val)
        v3 = v3.next

L = [L1,L2,L3]
sol = Solution()
result = sol.mergeKLists(L)
a = 1

#L1 = [1->4->5,1->3->4,2->6]
