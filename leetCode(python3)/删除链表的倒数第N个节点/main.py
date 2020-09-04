class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int)  -> ListNode:
        node_no = 0
        node = head
        while node is not None:
            node = node.next
            node_no += 1
        node_no -= n + 1

        node = head
        if node_no == -1:
            head = head.next
        else:
            while(node_no):
                node = node.next
                node_no -= 1
            node.next = node.next.next
        return head

array = [1,2,3,4,5]
L2 = 2
L1 = ListNode(None)
for i,val in enumerate(array):
    if i == 0:
        L1 = ListNode(val)
        v1 = L1
    else:
        v1.next = ListNode(val)
        v1 = v1.next
sol = Solution()
result = sol.removeNthFromEnd(L1,L2)
a = 1