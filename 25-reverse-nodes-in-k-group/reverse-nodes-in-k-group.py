# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      def finding_Kthnode(temp,k):
        k-=1
        while temp and k>0:
          temp=temp.next
          k-=1
        return temp
      def reversing(temp):
        prev=None
        cur=temp
        while cur:
          next_node=cur.next
          cur.next=prev
          prev=cur
          cur=next_node
        return prev
      def reversing_Kthnode(head,k):
        cur=head
        prevNode=None
        while cur:
          KthNode=finding_Kthnode(cur,k)
          if not KthNode:
            if prevNode:
              prevNode.next=cur
            break
          next_node=KthNode.next
          KthNode.next=None
          rnode=reversing(cur)
          if cur==head:
            head=KthNode
          else:
            prevNode.next=KthNode
          prevNode=cur
          cur=next_node
        return head

      return reversing_Kthnode(head,k) 