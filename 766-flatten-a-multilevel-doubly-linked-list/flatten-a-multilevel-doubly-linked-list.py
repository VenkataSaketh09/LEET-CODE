"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def children(self,node,bottom,next_node):
        cur=bottom
        while cur.next:
          if cur.child:
            self.children(cur,cur.child,cur.next)
          cur=cur.next
        node.next=bottom
        bottom.prev=node
        node.child=None
        cur.next=next_node
        if next_node:
          next_node.prev=cur
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
      temp=head
      while temp:
        if temp.child:
          next_node=temp.next
          self.children(temp,temp.child,next_node)
        temp=temp.next
      return head
        