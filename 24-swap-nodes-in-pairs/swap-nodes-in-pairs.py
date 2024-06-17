# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy=ListNode(0,head.next)
        temp=head
        prev=None
        while temp and temp.next:
            Next=temp.next
            temp.next,Next.next=Next.next,temp
            if prev:
                prev.next=Next
            prev=temp
            temp=temp.next
        return dummy.next

        