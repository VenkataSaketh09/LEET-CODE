# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s1=''
        temp=head
        while temp:
            s1+=str(temp.val)
            temp=temp.next
        s2=''.join(reversed(s1))
        if s1==s2:
            return True
        return False
        