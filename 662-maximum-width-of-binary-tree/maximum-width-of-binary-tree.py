# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      #level order traversal
      if not root:
        return 0
      queue=deque([(root,0)])
      max_width=0
      while queue:
        size=len(queue)
        num1,first_pos=queue[0]
        for i in range(size):
          node,pos=queue.popleft()
          if node.left:
            queue.append((node.left,2*pos))
          if node.right:
            queue.append((node.right,2*pos+1))
        last_pos=pos
        width=last_pos-first_pos+1
        max_width=max(max_width,width)
      return max_width





        