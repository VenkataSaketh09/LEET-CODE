# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      d=dict()
      if not head:
        return None
      temp=head
      while temp:
        d[temp.val]=d.get(temp.val,0)+1
        temp=temp.next
      dummy=ListNode(0)
      dummy.next=None
      ptr=dummy
      for key,value in d.items():
        if d[key]==1:
          ptr.next=ListNode(key)
          ptr=ptr.next
      return dummy.next    
        