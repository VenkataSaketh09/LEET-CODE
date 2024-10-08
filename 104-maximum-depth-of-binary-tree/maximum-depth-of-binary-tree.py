# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      def Depth(root):
        if not root:
          return 0
        left_height=Depth(root.left)
        right_height=Depth(root.right)

        return 1+max(left_height,right_height)
      return Depth(root)
        