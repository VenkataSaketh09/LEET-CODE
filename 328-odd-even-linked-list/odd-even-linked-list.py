# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        even_dummy=ListNode(0)
        odd_dummy=ListNode(0)
        even_ptr=even_dummy
        odd_ptr=odd_dummy
        ind=1
        while head:
            if ind%2!=0:
                odd_ptr.next=head
                odd_ptr=odd_ptr.next
            else:
                even_ptr.next=head
                even_ptr=even_ptr.next
            head=head.next
            ind+=1
        even_ptr.next=None
        odd_ptr.next=even_dummy.next
        return odd_dummy.next


        

        