# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,temp=head.next,head.next
        ans=0
        while temp:
            n=temp.val
            if n!=0:
                ans+=n
            else:
                prev.val=ans
                prev.next=temp.next
                prev=prev.next
                ans=0
            temp=temp.next
        return head.next

        