# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        ans=0
        set_nums=set(nums)
        flag=False
        while head:
            if head.val not in set_nums and flag:
                ans+=1
                flag=False
            elif head.val in set_nums:
                flag=True
            head=head.next
        if flag:
            ans+=1
        return ans
        