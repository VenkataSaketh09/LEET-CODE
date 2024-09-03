# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        nodes_lesser=ListNode(0)
        nodes_greater=ListNode(0)
        ptr1=nodes_lesser
        ptr2=nodes_greater
        cur=head
        while cur:
          if cur.val<x:
            ptr1.next=cur
            ptr1=ptr1.next
          else:
            ptr2.next=cur
            ptr2=ptr2.next
          cur=cur.next
        ptr1.next=nodes_greater.next
        ptr2.next=None
        return nodes_lesser.next