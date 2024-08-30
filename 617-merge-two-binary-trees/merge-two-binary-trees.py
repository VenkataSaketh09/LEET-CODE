# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
      if not root1:
        return root2
      que=deque([(root1,root2)])
      while que:
        node1,node2=que.popleft()

        if not node1 or not node2:
          continue
        
        node1.val=node1.val+node2.val

        if not node1.left:
          node1.left=node2.left
        else:
          que.append((node1.left,node2.left))
        
        if not node1.right:
          node1.right=node2.right
        else:
          que.append((node1.right,node2.right))
      return root1
        