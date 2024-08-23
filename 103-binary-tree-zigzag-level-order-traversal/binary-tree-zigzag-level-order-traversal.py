# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=deque()
        def bfs(root,level):
          if not root:
            return
          if level<=len(ans)-1 and level%2==0:
            ans[level].append(root.val)
          elif level<=len(ans)-1 and level%2!=0:
            ans[level].appendleft(root.val)
          else:
            ans.append(deque([root.val]))
          bfs(root.left,level+1)
          bfs(root.right,level+1)
        bfs(root,0)
        return ans