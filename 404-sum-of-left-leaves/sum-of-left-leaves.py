# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
      total=0

      def isLeaf(root):
        return root and not(root.left or root.right)
      
      def calculating(root):
        nonlocal total
        if not root:
          return 
        if isLeaf(root.left):
          total+=root.left.val
        calculating(root.left)
        calculating(root.right)
      calculating(root)
      return total