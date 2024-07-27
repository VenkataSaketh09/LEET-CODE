# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        ptr=None
        ptr1=ptr2=head
        while ptr2 and ptr2.next:
            ptr=ptr1
            ptr1=ptr1.next
            ptr2=ptr2.next.next
        ptr.next=None
        
        left=self.sortList(head)
        right=self.sortList(ptr1)
        
        return self.merging(left,right)
    
    def merging(self,list1,list2):
        dummy=ListNode(0)
        dummy.next=None
        temp=dummy
        
        while list1 and list2:
            if list1.val>list2.val:
                temp.next=list2
                list2=list2.next
            else:
                temp.next=list1
                list1=list1.next
            temp=temp.next
        if list1:
            temp.next=list1
        if list2:
            temp.next=list2
        return dummy.next
        