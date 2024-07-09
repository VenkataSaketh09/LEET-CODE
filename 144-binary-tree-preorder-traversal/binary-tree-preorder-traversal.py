# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def dfs(current_node,ans):
            if current_node:
                ans.append(current_node.val)
                dfs(current_node.left,ans)
                dfs(current_node.right,ans)
        dfs(root,ans)
        return ans
        
        