# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr1=ptr2=head
        if head is None or head.next is None:
            return head
        for i in range(k-1):
            if ptr1 is None:
                return head
            ptr1=ptr1.next
        val1=ptr1
        ptr1=ptr1.next

        while ptr1:
            ptr1=ptr1.next
            ptr2=ptr2.next
        val2=ptr2
        val1.val,val2.val=val2.val,val1.val
        return head

        