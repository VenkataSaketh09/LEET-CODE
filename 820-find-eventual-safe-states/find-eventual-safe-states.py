class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
      def dfs(node):
        if states[node]==1:
          return False
        if states[node]==3:
          return True
        states[node]=1 #visiting
        for neighbor in graph[node]:
          if not dfs(neighbor): # returns True if it is  a part of cycle or leading to cyle
            states[node]=2
            return False
        states[node]=3
        return True

      n=len(graph)
      safe_nodes=[]
      states=[0]*n
      #0:unvisited 1:visitin 2:unsafe 3:safe
      for i in range(n):
        if dfs(i):
          safe_nodes.append(i)
      return sorted(safe_nodes)