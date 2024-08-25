# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
      arr=[]
      min_diff=float('inf')
      def inorder(root):
        if not root:
          return
        inorder(root.left)
        arr.append(root.val)
        inorder(root.right)
      inorder(root)
      if len(arr)<2:
        return 0
      for i in range(1,len(arr)):
        val=abs(arr[i]-arr[i-1])
        if val<=min_diff:
          min_diff=val
      return min_diff


        