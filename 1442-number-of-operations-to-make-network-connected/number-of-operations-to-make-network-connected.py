class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
      if len(connections)<n-1:
        return -1
      adjacency_list={i:[] for i in range(n)}
      for node1,node2 in connections:
        adjacency_list[node1].append(node2)
        adjacency_list[node2].append(node1)
      def dfs(node,visited):
        visited.add(node)
        for neighbor in adjacency_list[node]:
          if neighbor not in visited:
            dfs(neighbor,visited)
      visited=set()
      count=0
      for i in range(n):
        if i not in visited:
          dfs(i,visited)
          count+=1
      return count-1