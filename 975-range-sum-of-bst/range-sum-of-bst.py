# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
      #dfs traversal
      def dfs(node):
        if not node:
          return 0
        cur_val=0
        if low<=node.val<=high:
          cur_val=node.val
        left_sum=dfs(node.left)
        right_sum=dfs(node.right)
        
        return cur_val+left_sum+right_sum
      return dfs(root)
       


        