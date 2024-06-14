# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        temp=head
        length=1
        while temp.next:
            length+=1
            temp=temp.next
        temp.next=head
        cut=length-(k%length)
        while cut>1:
            head=head.next
            cut-=1
        temp=head.next
        head.next=None
        return temp

        
        