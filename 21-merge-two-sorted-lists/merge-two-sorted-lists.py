# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        ptr=dummy
        temp1=list1
        temp2=list2
        while temp1 and temp2:
          if temp1.val<=temp2.val:
            ptr.next=temp1
            temp1=temp1.next
          else:
            ptr.next=temp2
            temp2=temp2.next
          ptr=ptr.next
        while temp1:
          ptr.next=temp1
          temp1=temp1.next
          ptr=ptr.next
        while temp2:
          ptr.next=temp2
          temp2=temp2.next
          ptr=ptr.next
        return dummy.next

        