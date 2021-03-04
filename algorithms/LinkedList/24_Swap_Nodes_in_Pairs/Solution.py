# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prehead = ListNode(next=head)
        lastpair = prehead
        p1 = head
        while(p1 and p1.next):
            # swap p1 and p2
            p2 = p1.next
            p1.next = p2.next
            p2.next = p1
            lastpair.next = p2
            lastpair = p1
            p1 = p1.next
        return prehead.next
