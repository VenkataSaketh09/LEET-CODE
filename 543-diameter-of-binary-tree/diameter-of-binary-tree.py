# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      ans=0
      def diameter(root):
        if not root:
          return 0
        nonlocal ans
        left_depth=diameter(root.left)
        right_depth=diameter(root.right)
        ans=max(ans,left_depth+right_depth)
        return 1+max(left_depth,right_depth)
      diameter(root)
      return ans

        