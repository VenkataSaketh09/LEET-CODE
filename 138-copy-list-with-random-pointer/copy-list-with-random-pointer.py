"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
      if not head:
        return None
      copied_nodes={}
      temp=head
      while temp:
        copied_nodes[temp]=Node(temp.val)
        temp=temp.next
      temp=head
      while temp:
        copied_nodes[temp].next=copied_nodes.get(temp.next)
        copied_nodes[temp].random=copied_nodes.get(temp.random)
        temp=temp.next
      return copied_nodes[head]
        