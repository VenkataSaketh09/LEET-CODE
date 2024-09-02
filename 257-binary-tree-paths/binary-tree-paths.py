# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
      def constructing(node,path):
        if node:
          path+=str(node.val)
          if not node.left and not node.right:
            ans.append(path)
          else:
            path+='->'
            constructing(node.left,path)
            constructing(node.right,path)
      ans=[]
      constructing(root,"")
      return ans
        