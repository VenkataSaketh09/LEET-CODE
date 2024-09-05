# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head
        while fast and fast.next:
          slow=slow.next
          fast=fast.next.next
        cur=slow.next
        slow.next=None
        prev=None
        while cur:
          next_node=cur.next
          cur.next=prev
          prev=cur
          cur=next_node
        first=head
        second=prev
        while second:
          first_next,second_next=first.next,second.next
          first.next=second
          second.next=first_next
          first,second=first_next,second_next
        return head

        