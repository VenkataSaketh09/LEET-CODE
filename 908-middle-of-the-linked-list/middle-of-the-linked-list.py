# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp=head
        # count=0
        # while temp:
        #     temp=temp.next
        #     count+=1
        # mid=count//2
        # temp=head
        # for _ in range(mid):
        #     temp=temp.next
        # return temp

        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

        
            

        

        