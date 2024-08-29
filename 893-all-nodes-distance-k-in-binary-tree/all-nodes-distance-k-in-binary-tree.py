# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict,deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
      if not root:
        return []
      graph=defaultdict(list)

      def constructing_graph(node,parent):
        if node:
          if parent:
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)
          constructing_graph(node.left,node)
          constructing_graph(node.right,node)
      constructing_graph(root,None)

      visited=set([target.val])
      ans=[]
      que=deque([(target.val,0)])

      while que:
        node,dist=que.popleft()

        if dist==k:
          ans.append(node)
        if dist>k:
          break
        
        for neighbor in graph[node]:
          if neighbor not in visited:
            visited.add(neighbor)
            que.append((neighbor,dist+1))
      return ans

        