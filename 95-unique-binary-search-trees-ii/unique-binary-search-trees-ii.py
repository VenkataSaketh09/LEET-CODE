# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
      def constructing_trees(start,end):
        if start>end:
          return [None,]
        trees_list=[]
        for i in range(start,end+1):
          left_trees=constructing_trees(start,i-1)
          right_trees=constructing_trees(i+1,end)

          for left_side in left_trees:
            for right_side in right_trees:
              cur_node=TreeNode(i)
              cur_node.left=left_side
              cur_node.right=right_side
              trees_list.append(cur_node)
        return trees_list
      return constructing_trees(1,n) if n else []


        