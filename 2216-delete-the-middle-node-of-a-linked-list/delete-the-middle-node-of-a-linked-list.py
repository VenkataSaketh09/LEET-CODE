# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # count=1
        # temp=head
        # if not head or not head.next:
        #     return head.next
        # while temp.next:
        #     count+=1
        #     temp=temp.next
        # ind=(count//2)
        # if ind==0:
        #     return head.next
        # temp=head
        # for _ in range(ind-1):
        #     temp=temp.next
        # if temp.next and temp.next.next:
        #     temp.next = temp.next.next
        # else:
        #     temp.next = None
        # return head
        dummy=ListNode(0)
        dummy.next=head
        slow=dummy
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return dummy.next
        