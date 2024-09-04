# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      def Depth(root):
        if not root:
          return 0
        left_height=Depth(root.left)
        right_height=Depth(root.right)
        if left_height==-1 or right_height==-1:
          return -1
        elif (abs(left_height-right_height)>1):
          return -1
        return 1+max(left_height,right_height)
      return Depth(root)!=-1
        