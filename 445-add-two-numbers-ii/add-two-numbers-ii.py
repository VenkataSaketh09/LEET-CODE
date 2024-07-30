# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      stack1=[]
      stack2=[]
      dummy=ListNode(0)
      dummy.next=None
      carry=0
      ptr=dummy
      while l1 or l2:
        stack1.append(l1.val) if l1 else 0
        stack2.append(l2.val)  if l2 else 0
        l1=l1.next if l1 else None
        l2=l2.next if l2 else None
      while stack1 or stack2 or carry:
        val1=stack1.pop() if len(stack1) else 0
        val2=stack2.pop() if len(stack2) else 0
        total_val=val1+val2+carry
        digit=total_val%10
        carry=total_val//10

        ptr.next=ListNode(digit)
        ptr=ptr.next
      return self.reversing(dummy.next)
    def reversing(self,head:Optional[ListNode])->Optional[ListNode]:
      prev=None
      curr=head
      while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
      return prev

      
        