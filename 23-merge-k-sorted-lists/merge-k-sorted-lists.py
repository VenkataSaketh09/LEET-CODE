# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      if lists==[] or lists==[[]]:
        return None
      temp=[]
      for data in lists:
        nums=data
        while nums:
          temp.append(nums.val)
          nums=nums.next
      temp.sort()
      head=None
      for data in temp:
        if head is None:
          head=ListNode(data)
          ptr=head
        else:
          dummy=ListNode(data)
          ptr.next=dummy
          ptr=ptr.next
      return head

        